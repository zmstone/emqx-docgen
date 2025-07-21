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
    output_dir = Path('docs/examples') / version_tag
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
