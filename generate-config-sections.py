#!/usr/bin/env python3

import argparse
import json
import os
from pathlib import Path
import sys
from typing import List, Dict

# maps section names to the tags that should compose it.
special_sections_tags_ce = {
    "emqx": "EMQX",
    "authn": "Authentication",
    "authz": "Authorization",
    "bridges": "Bridge",
    "rule": "Rule Engine",
    "gateway": "Gateway",
}
special_sections_tags_ee = {
    **special_sections_tags_ce,
    "license": "License",
}


def get_structs_with_tags(full_schema: List[Dict], tags: List[str]) -> List[Dict]:
    return [struct for struct in full_schema if set(tags).issubset(set(struct["tags"]))]


def get_structs_without_tags(full_schema: List[Dict], tags: List[str]) -> List[Dict]:
    return [
        struct for struct in full_schema if set(tags).isdisjoint(set(struct["tags"]))
    ]


def ensure_dir(dir_path: Path):
    try:
        os.makedirs(dir_path)
    except FileExistsError:
        pass


def dir_path(path_str: str, **kwargs) -> Path:
    path = Path(path_str)
    if path.is_dir():
        return path
    else:
        if kwargs.get("create", False):
            ensure_dir(path)
            return path
        else:
            raise argparse.ArgumentTypeError(f"{path} must be a directory")


def find_schema_json(root_dir: Path, profile: str) -> Path:
    path = (
        # starting from v5.0.21
        root_dir / "_build/docgen" / profile / "schema-en.json"
    )
    if path.is_file():
        return path
    else:
        raise RuntimeError(
            f"schema.json not found in {path}\n"
            "did you forget to run `make emqx{,-enterprise}`?"
        )


def assert_non_empty(special_sections: Dict):
    for slug, subsection in special_sections.items():
        if not subsection:
            raise RuntimeError(f"section {slug} is empty!")


def main(argv):
    parser = argparse.ArgumentParser(
        description="Given a JSON schema of EMQX's configuration,"
        " split it into subsections"
    )
    parser.add_argument(
        "-p",
        "--project-root",
        required=True,
        help="path to the EMQX (5.0) project root",
        type=dir_path,
    )
    parser.add_argument(
        "--profile",
        required=True,
        help="The EMQX build profile",
        choices=["emqx", "emqx-enterprise"],
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        required=False,
        default="dist",
        help="path to output the subsection JSONs",
        type=lambda path: dir_path(path, create=True),
    )
    parser.add_argument(
        "-v",
        "--version",
        required=True,
        help="the version of EMQX",
    )
    args = parser.parse_args(argv)
    schema_path = find_schema_json(args.project_root, args.profile)
    with open(schema_path) as f:
        full_schema = json.load(f)

    if args.profile == "emqx":
        special_sections_tags = special_sections_tags_ce
    elif args.profile == "emqx-enterprise":
        special_sections_tags = special_sections_tags_ee
    else:
        raise RuntimeError(f"unknown profile: {args.profile}")

    special_sections = {
        slug: get_structs_with_tags(full_schema, [tag])
        for slug, tag in special_sections_tags.items()
    }
    assert_non_empty(special_sections)
    special_tags = list(special_sections_tags.values())
    root, *generic_section = get_structs_without_tags(full_schema, special_tags)
    all_sections = {**special_sections, "others": generic_section}
    all_sections["emqx"] = [root] + all_sections["emqx"]
    for slug, subjson in all_sections.items():
        output_dir = args.output_dir / args.version / "json"
        output = output_dir / f"{slug}.json"
        ensure_dir(output_dir)
        print(f"writing output to {output}")
        with open(output, "w") as f:
            json.dump(subjson, f, indent=2, sort_keys=True)


if __name__ == "__main__":
    main(sys.argv[1:])
