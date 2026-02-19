# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "requests",
#     "openai",
# ]
# ///

import argparse
import hashlib
import json
import os
import shutil
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
from openai import OpenAI

PROMPT_URL = (
    "https://gist.githubusercontent.com/zmstone/44747c1adc7f86ca1968f4bf4f16307b/raw/"
    "emqx-config-example-generation-prompt.txt"
)
ROOT_STRUCT_NAME = "emqx:Root Config Keys"
thread_local = threading.local()


def setup_openai(api_key):
    return OpenAI(api_key=api_key)


def get_openai_client(api_key):
    client = getattr(thread_local, "openai_client", None)
    if client is None:
        client = setup_openai(api_key)
        thread_local.openai_client = client
    return client


def load_schema(schema_path):
    with open(schema_path, "r") as f:
        return json.load(f)


def get_system_prompt():
    try:
        response = requests.get(PROMPT_URL, timeout=20)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error downloading prompt: {e}")
        return None


def extract_response_text(response):
    output_text = getattr(response, "output_text", None)
    if isinstance(output_text, str) and output_text.strip():
        return output_text

    output = getattr(response, "output", None) or []
    parts = []
    for out in output:
        for content in (getattr(out, "content", None) or []):
            text = getattr(content, "text", None)
            if isinstance(text, str) and text.strip():
                parts.append(text)
                continue
            text = getattr(content, "output_text", None)
            if isinstance(text, str) and text.strip():
                parts.append(text)
                continue
            text = getattr(content, "value", None)
            if isinstance(text, str) and text.strip():
                parts.append(text)

    if parts:
        return "\n".join(parts)
    return None


def slim_field_type(field_type):
    kind = field_type.get("kind")
    if kind == "struct":
        return {"kind": "struct", "name": field_type.get("name")}
    if kind in ("primitive", "singleton"):
        return {"kind": kind, "name": field_type.get("name")}
    if kind == "enum":
        return {"kind": "enum", "symbols": field_type.get("symbols", [])}
    if kind == "array":
        return {"kind": "array", "elements": slim_field_type(field_type.get("elements", {}))}
    if kind == "map":
        return {
            "kind": "map",
            "name": field_type.get("name"),
            "values": slim_field_type(field_type.get("values", {})),
        }
    if kind == "union":
        return {
            "kind": "union",
            "members": [slim_field_type(m) for m in field_type.get("members", [])],
        }
    return {"kind": kind}


def slim_struct(struct):
    fields = []
    for field in struct.get("fields", []):
        slim_field = {
            "name": field.get("name"),
            "type": slim_field_type(field.get("type", {})),
        }
        for key in ("desc", "raw_default", "default", "aliases", "importance", "deprecated", "extra"):
            if key in field:
                slim_field[key] = field[key]
        fields.append(slim_field)

    result = {
        "full_name": struct.get("full_name"),
        "fields": fields,
    }
    if "desc" in struct:
        result["desc"] = struct["desc"]
    if "paths" in struct:
        result["paths"] = struct["paths"]
    if "tags" in struct:
        result["tags"] = struct["tags"]
    return result


def make_cache_key(model, prompt, struct):
    payload = {
        "model": model,
        "prompt": prompt,
        "struct": slim_struct(struct),
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def load_cached_example(cache_dir, cache_key):
    path = cache_dir / f"{cache_key}.json"
    if not path.exists():
        return None
    try:
        with open(path, "r") as f:
            payload = json.load(f)
        content = payload.get("content")
        if isinstance(content, str) and content.strip():
            return content
    except Exception:
        pass
    return None


def save_cached_example(cache_dir, cache_key, struct_name, content):
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / f"{cache_key}.json"
    payload = {
        "struct_name": struct_name,
        "content": content,
        "updated_at": int(time.time()),
    }
    with open(path, "w") as f:
        json.dump(payload, f, ensure_ascii=False)


def generate_example(struct, api_key, model, prompt, retries=3):
    client = get_openai_client(api_key)
    input_messages = [
        {"role": "system", "content": prompt},
        {
            "role": "user",
            "content": "Please generate a valid HOCON example for this schema:\n"
            + json.dumps(slim_struct(struct), indent=2),
        },
    ]

    for attempt in range(1, retries + 1):
        try:
            request = {
                "model": model,
                "input": input_messages,
            }
            # Some reasoning/codex models reject temperature.
            supports_temperature = not (
                model.startswith("o")
                or model.startswith("gpt-5")
                or "codex" in model
            )
            if supports_temperature:
                request["temperature"] = 0.7

            response = client.responses.create(**request)
            content = extract_response_text(response)
            if content:
                return content
            raise RuntimeError("No text content returned by model")
        except Exception as e:
            if attempt >= retries:
                print(f"Error generating example for {struct.get('full_name')}: {e}")
                return None
            sleep_s = min(8, 2 ** (attempt - 1))
            print(
                f"Retrying {struct.get('full_name')} ({attempt}/{retries - 1}) after error: {e}"
            )
            time.sleep(sleep_s)


def save_example(content, output_dir, struct_name):
    if not content:
        return False

    filename = struct_name.replace(":", "-") + ".hocon"
    filepath = output_dir / filename

    try:
        with open(filepath, "w") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error saving file {filepath}: {e}")
        return False


def build_schema_lookup(schema_data):
    lookup = {}
    for struct in schema_data:
        lookup[struct["full_name"]] = struct
    return lookup


def structs_are_equal(struct1, struct2):
    return json.dumps(struct1, sort_keys=True) == json.dumps(struct2, sort_keys=True)


def get_example_filename(struct_name):
    return struct_name.replace(":", "-") + ".hocon"


def copy_example_from_base(base_dir, output_dir, struct_name):
    filename = get_example_filename(struct_name)
    source_file = base_dir / filename
    dest_file = output_dir / filename

    if not source_file.exists():
        return False

    try:
        shutil.copy2(source_file, dest_file)
        return True
    except Exception as e:
        print(f"Error copying file from {source_file} to {dest_file}: {e}")
        return False


def resolve_base_schema_path(base_schema_dir, base_version):
    candidates = [
        base_schema_dir / f"{base_version}.json",
        base_schema_dir / f"v{base_version}.json",
        base_schema_dir / f"e{base_version}.json",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None, candidates


def main():
    parser = argparse.ArgumentParser(description="Generate HOCON examples from schema")
    parser.add_argument("schema_path", help="Path to the schema JSON file")
    parser.add_argument(
        "--api-key",
        help="OpenAI API key (can also be set via OPENAI_API_KEY env var)",
        required=False,
    )
    parser.add_argument(
        "--model",
        default="gpt-5.2-codex",
        help="OpenAI model to use (default: gpt-5.2-codex)",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Concurrent workers for generation (default: 4)",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Disable cache lookup/save for generated examples",
    )
    parser.add_argument(
        "-b",
        "--compare-base",
        help=(
            "Base version to compare against (e.g., 5.8.5). "
            "If schema unchanged, copy example from base directory."
        ),
        required=False,
    )
    parser.add_argument(
        "--list-changes",
        action="store_true",
        help="List changed schemas without generating examples. Requires --compare-base.",
    )
    args = parser.parse_args()

    if args.list_changes and not args.compare_base:
        print("Error: --list-changes requires --compare-base to be specified")
        return

    api_key = None
    if not args.list_changes:
        api_key = os.getenv("OPENAI_API_KEY") or args.api_key
        if not api_key:
            print(
                "Error: OpenAI API key must be provided via --api-key or OPENAI_API_KEY environment variable"
            )
            return

    schema_path = Path(args.schema_path)
    if not schema_path.exists():
        print(f"Schema file not found: {schema_path}")
        return

    version_tag = schema_path.stem.lstrip("ve")

    output_dir = None
    cache_dir = None
    if not args.list_changes:
        output_dir = Path("docs/examples") / version_tag
        output_dir.mkdir(parents=True, exist_ok=True)
        cache_dir = output_dir / ".cache"

    base_schema_lookup = None
    base_examples_dir = None
    if args.compare_base:
        base_schema_dir = schema_path.parent
        resolved = resolve_base_schema_path(base_schema_dir, args.compare_base)
        if isinstance(resolved, tuple):
            base_schema_path, candidates = resolved
        else:
            base_schema_path = resolved
            candidates = []

        if not base_schema_path:
            candidate_names = ", ".join([p.name for p in candidates])
            print(
                f"Warning: Base schema file not found for version {args.compare_base}. "
                f"Checked: {candidate_names}. Will generate all examples from scratch."
            )
        else:
            print(f"Loading base schema from: {base_schema_path}")
            base_schema_data = load_schema(base_schema_path)
            base_schema_lookup = build_schema_lookup(base_schema_data)
            base_examples_dir = Path("docs/examples") / args.compare_base
            if not base_examples_dir.exists() and not args.list_changes:
                print(
                    f"Warning: Base examples directory not found: {base_examples_dir}. "
                    "Will generate all examples from scratch."
                )
                base_examples_dir = None

    schema_data = load_schema(schema_path)

    if args.list_changes:
        if not base_schema_lookup:
            print("Error: Could not load base schema for comparison")
            return

        changed_schemas = []
        new_schemas = []
        unchanged_schemas = []
        removed_schemas = []

        new_schema_lookup = build_schema_lookup(schema_data)

        for struct in schema_data[1:]:
            struct_name = struct["full_name"]
            base_struct = base_schema_lookup.get(struct_name)

            if base_struct:
                if structs_are_equal(struct, base_struct):
                    unchanged_schemas.append(struct_name)
                else:
                    changed_schemas.append(struct_name)
            else:
                new_schemas.append(struct_name)

        for struct_name in base_schema_lookup.keys():
            if struct_name not in new_schema_lookup and struct_name != ROOT_STRUCT_NAME:
                removed_schemas.append(struct_name)

        print("\n=== Schema Comparison Results ===")
        print(f"Base version: {args.compare_base}")
        print(f"New version: {version_tag}\n")

        if changed_schemas:
            print(f"Changed schemas ({len(changed_schemas)}):")
            for name in sorted(changed_schemas):
                print(f"  - {name}")
            print()

        if new_schemas:
            print(f"New schemas ({len(new_schemas)}):")
            for name in sorted(new_schemas):
                print(f"  - {name}")
            print()

        if removed_schemas:
            print(f"Removed schemas ({len(removed_schemas)}):")
            for name in sorted(removed_schemas):
                print(f"  - {name}")
            print()

        print(f"Unchanged schemas: {len(unchanged_schemas)}")
        print(f"Total schemas in new version: {len(schema_data) - 1}")
        print(f"Total schemas in base version: {len(base_schema_lookup) - 1}")
        return

    prompt = get_system_prompt()
    if not prompt:
        print("Error: failed to fetch system prompt")
        return

    stats = {
        "copied": 0,
        "cached": 0,
        "generated": 0,
        "failed": 0,
    }

    to_generate = []

    for struct in schema_data[1:]:
        struct_name = struct["full_name"]

        should_generate = True
        if base_schema_lookup and base_examples_dir and base_examples_dir.exists():
            base_struct = base_schema_lookup.get(struct_name)
            if base_struct and structs_are_equal(struct, base_struct):
                if copy_example_from_base(base_examples_dir, output_dir, struct_name):
                    stats["copied"] += 1
                    print(f"Copied unchanged example for {struct_name} from base version")
                    should_generate = False
                else:
                    print(
                        f"Schema unchanged for {struct_name} but base example missing; will generate."
                    )

        if should_generate:
            to_generate.append(struct)

    if to_generate:
        print(
            f"\nGenerating {len(to_generate)} examples with model={args.model}, workers={args.workers}, cache={'off' if args.no_cache else 'on'}"
        )

    def worker(struct):
        struct_name = struct["full_name"]
        cache_key = make_cache_key(args.model, prompt, struct)

        if not args.no_cache:
            cached = load_cached_example(cache_dir, cache_key)
            if cached:
                if save_example(cached, output_dir, struct_name):
                    return struct_name, "cached"

        content = generate_example(struct, api_key, args.model, prompt)
        if not content:
            return struct_name, "failed"

        if save_example(content, output_dir, struct_name):
            if not args.no_cache:
                try:
                    save_cached_example(cache_dir, cache_key, struct_name, content)
                except Exception as e:
                    print(f"Warning: failed to save cache for {struct_name}: {e}")
            return struct_name, "generated"
        return struct_name, "failed"

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(worker, struct): struct["full_name"] for struct in to_generate}
        for future in as_completed(futures):
            struct_name = futures[future]
            try:
                _, status = future.result()
            except Exception as e:
                print(f"Unexpected failure for {struct_name}: {e}")
                stats["failed"] += 1
                continue

            stats[status] += 1
            if status == "generated":
                print(f"Generated: {struct_name}")
            elif status == "cached":
                print(f"Cache hit: {struct_name}")
            else:
                print(f"Failed: {struct_name}")

    print("\n=== Generation Summary ===")
    print(f"Copied unchanged examples: {stats['copied']}")
    print(f"Loaded from cache: {stats['cached']}")
    print(f"Generated from model: {stats['generated']}")
    print(f"Failed: {stats['failed']}")


if __name__ == "__main__":
    main()
