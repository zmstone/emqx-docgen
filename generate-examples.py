import json
import os
import time
import argparse
from pathlib import Path
from openai import OpenAI

def setup_openai(api_key):
    return OpenAI(api_key=api_key)

def load_schema(schema_path):
    with open(schema_path, 'r') as f:
        return json.load(f)

def get_system_prompt():
    return """You are a helpful assistant that generates HOCON format examples based the schema specification.

Below is the schema format:
- Each schema is a JSON object to describe a struct kind type.
- The "paths" field is an array of dot-separated strings that describes the value path to the field from the config root.
- For structs, the "fields" field is an object to describe the fields of the struct.
- For each struct, there can be a "desc" field to describe the struct in human-readable format.
- For each field:
  - For "struct" kind, the "name" field is the reference to the sub-struct.
  - Other than "struct" or "map" kind, the other complex types are "array" and "union" (oneOf).
  - The "default" and "raw_default" fields are the default value of the field if it is not provided, you should generate the example based on the "default" field.
  - If "default" or "raw_default" are empty, the "desc" field is to be used as hints to generate the example.

Below are the requirements for the generated example:
- If a field has a "desc" field that starts with "Deprecated", it's a deprecated field, hence you should not generate an example for it.
- Always generate example for a struct with it's path and {} around the fields with proper indentation. For example:
  value.path.to.sturct {
    field1 = ...
    field2 = ...
  }
- If a field type is a union of sub-structs or a reference to a sub-struct, generate its example using placeholders inside "{" and "}". Each placeholder is a HOCON comment like "#substruct(<reference_name>)" in a new line with proper indentation. For example:
  value.path.to.sturct {
    #substruct(namespace1:substruct1)
    #substruct(namespace2:substruct2)
  }
- If a union member is not a substruct, simply generate a config value for the union member.
- For map, the key is a dollar ($) sign prefixed placehocer such as "$name", you should generate a sensible example key for the map based on the path of the field. For example, if the path is "webhook.name", the key should be "mywebhook1".
- While colon is a valid delimiter for key-value pair, you should use "=" as the delimiter in the generated example.
- I prefer to have clean examples, so no need to include comments in the generated example.
- Do not quote the generated example in backticks.
- If the path has "$INDEX" in it, it is an array, use array syntax like field = [...] instead of using index number as key.
- The type information is inherited from Eralng type specs, so you should generate the example based on the type specs. For example "binary()" is binary string, etc.
- The bytes configs such as "1MB", and duration configs such as "1d" should be quoted.
- After generated, go through the requirements and make sure the generated example meets all the above requirements."""

def generate_example(struct, openai):
    try:
        # Skip top level struct, use its fields directly
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": get_system_prompt()},
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

def main():
    parser = argparse.ArgumentParser(description='Generate HOCON examples from schema')
    parser.add_argument('schema_path', help='Path to the schema JSON file')
    parser.add_argument('--api-key', help='OpenAI API key (can also be set via OPENAI_API_KEY env var)', required=False)
    args = parser.parse_args()

    # Get API key from environment variable or command line argument
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

    # Setup output directory
    output_dir = Path('examples') / version_tag
    output_dir.mkdir(parents=True, exist_ok=True)

    # Setup OpenAI
    openai = setup_openai(api_key)

    # Load schema
    schema_data = load_schema(schema_path)

    # Skip the first schema (logical root) and process all other types
    for struct in schema_data[1:]:
        print(f"Processing: {struct['full_name']}...")

        # Generate example
        example_content = generate_example(struct, openai)

        # Save example
        if save_example(example_content, output_dir, struct['full_name']):
            print(f"Successfully generated example for {struct['full_name']}")
        else:
            print(f"Failed to generate example for {struct['full_name']}")

        # Rate limiting
        time.sleep(1)

if __name__ == "__main__":
    main()
