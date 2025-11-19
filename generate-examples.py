# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "requests",
#     "openai",
# ]
# ///

import json
import os
import time
import argparse
import requests
import shutil
from pathlib import Path
from openai import OpenAI

def setup_openai(api_key):
    return OpenAI(api_key=api_key)

def load_schema(schema_path):
    with open(schema_path, 'r') as f:
        return json.load(f)

def get_system_prompt():
    url = "https://gist.githubusercontent.com/zmstone/44747c1adc7f86ca1968f4bf4f16307b/raw/emqx-config-example-generation-prompt.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except Exception as e:
        print(f"Error downloading prompt: {e}")
        return None

def generate_example(struct, openai):
    try:
        prompt = get_system_prompt()
        if not prompt:
            return None

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Please generate a valid HOCON example for this schema:\n{json.dumps(struct, indent=2)}"}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating example: {e}")
        return None

def save_example(content, output_dir, struct_name):
    if not content:
        return False

    # Replace colons with hyphens in the filename
    filename = struct_name.replace(':', '-') + '.hocon'
    filepath = output_dir / filename

    try:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error saving file {filepath}: {e}")
        return False

def build_schema_lookup(schema_data):
    """Build a dictionary mapping full_name to struct for quick lookup."""
    lookup = {}
    for struct in schema_data:
        lookup[struct['full_name']] = struct
    return lookup

def structs_are_equal(struct1, struct2):
    """Compare two structs by their JSON representation."""
    return json.dumps(struct1, sort_keys=True) == json.dumps(struct2, sort_keys=True)

def get_example_filename(struct_name):
    """Get the example filename for a struct name."""
    return struct_name.replace(':', '-') + '.hocon'

def copy_example_from_base(base_dir, output_dir, struct_name):
    """Copy example file from base directory to output directory."""
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

def main():
    parser = argparse.ArgumentParser(description='Generate HOCON examples from schema')
    parser.add_argument('schema_path', help='Path to the schema JSON file')
    parser.add_argument('--api-key', help='OpenAI API key (can also be set via OPENAI_API_KEY env var)', required=False)
    parser.add_argument('-b', '--compare-base', help='Base version to compare against (e.g., 5.8.5). If schema unchanged, copy example from base directory.', required=False)
    parser.add_argument('--list-changes', action='store_true', help='List changed schemas without generating examples. Requires --compare-base.')
    args = parser.parse_args()

    # Validate list-changes requires compare-base
    if args.list_changes and not args.compare_base:
        print("Error: --list-changes requires --compare-base to be specified")
        return

    # Get API key from environment variable or command line argument (only needed if not listing changes)
    api_key = None
    if not args.list_changes:
        api_key = os.getenv('OPENAI_API_KEY') or args.api_key
        if not api_key:
            print("Error: OpenAI API key must be provided via --api-key or OPENAI_API_KEY environment variable")
            return

    schema_path = Path(args.schema_path)
    if not schema_path.exists():
        print(f"Schema file not found: {schema_path}")
        return

    # Extract version tag from schema filename and remove v/e prefix
    version_tag = schema_path.stem.lstrip('ve')

    # Setup output directory (only needed if not listing changes)
    output_dir = None
    if not args.list_changes:
        output_dir = Path('docs/examples') / version_tag
        output_dir.mkdir(parents=True, exist_ok=True)

    # Load base schema and setup base directory if compare-base is provided
    base_schema_lookup = None
    base_examples_dir = None
    if args.compare_base:
        # Find base schema file (could be v{version} or e{version})
        base_schema_dir = schema_path.parent
        base_schema_v = base_schema_dir / f"v{args.compare_base}.json"
        base_schema_e = base_schema_dir / f"e{args.compare_base}.json"

        base_schema_path = None
        if base_schema_v.exists():
            base_schema_path = base_schema_v
        elif base_schema_e.exists():
            base_schema_path = base_schema_e
        else:
            print(f"Warning: Base schema file not found for version {args.compare_base}. Will generate all examples from scratch.")

        if base_schema_path:
            print(f"Loading base schema from: {base_schema_path}")
            base_schema_data = load_schema(base_schema_path)
            base_schema_lookup = build_schema_lookup(base_schema_data)
            base_examples_dir = Path('docs/examples') / args.compare_base
            if not base_examples_dir.exists() and not args.list_changes:
                print(f"Warning: Base examples directory not found: {base_examples_dir}. Will generate all examples from scratch.")
                base_examples_dir = None

    # Load schema
    schema_data = load_schema(schema_path)

    # If listing changes, analyze and print without generating
    if args.list_changes:
        if not base_schema_lookup:
            print("Error: Could not load base schema for comparison")
            return

        changed_schemas = []
        new_schemas = []
        unchanged_schemas = []
        removed_schemas = []

        # Build lookup for new schema
        new_schema_lookup = build_schema_lookup(schema_data)

        # Check schemas in new version
        for struct in schema_data[1:]:  # Skip the first schema (logical root)
            struct_name = struct['full_name']
            base_struct = base_schema_lookup.get(struct_name)

            if base_struct:
                if structs_are_equal(struct, base_struct):
                    unchanged_schemas.append(struct_name)
                else:
                    changed_schemas.append(struct_name)
            else:
                new_schemas.append(struct_name)

        # Check for removed schemas (in base but not in new)
        for struct_name in base_schema_lookup.keys():
            if struct_name not in new_schema_lookup:
                # Skip the root config
                if struct_name != "emqx:Root Config Keys":
                    removed_schemas.append(struct_name)

        # Print results
        print(f"\n=== Schema Comparison Results ===")
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

    # Setup OpenAI for example generation
    openai = setup_openai(api_key)

    # Skip the first schema (logical root) and process all other types
    for struct in schema_data[1:]:
        struct_name = struct['full_name']
        print(f"Processing: {struct_name}...")

        # Check if we can reuse base example
        should_generate = True
        if base_schema_lookup and base_examples_dir and base_examples_dir.exists():
            base_struct = base_schema_lookup.get(struct_name)
            if base_struct and structs_are_equal(struct, base_struct):
                # Schema unchanged, try to copy from base
                if copy_example_from_base(base_examples_dir, output_dir, struct_name):
                    print(f"Copied unchanged example for {struct_name} from base version")
                    should_generate = False
                else:
                    print(f"Schema unchanged but example file not found in base, generating new one...")
            elif base_struct:
                print(f"Schema changed for {struct_name}, generating new example...")
            else:
                print(f"New schema {struct_name} not in base version, generating new example...")

        # Generate example if needed
        if should_generate:
            example_content = generate_example(struct, openai)

            # Save example
            if save_example(example_content, output_dir, struct_name):
                print(f"Successfully generated example for {struct_name}")
            else:
                print(f"Failed to generate example for {struct_name}")

            # Rate limiting
            time.sleep(1)

if __name__ == "__main__":
    main()
