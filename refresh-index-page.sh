#!/bin/bash

index_file="index.html"

cd "$(dirname "$0")"

cd docs/

# Initialize the index file with an HTML header
echo "<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Index of HTML files</title>
</head>
<body>
  <h1>Index of HTML files</h1>
  <ul>" > $index_file

# Find all HTML files in the subdirectories and create a list with links
find -type f -iname "*.html" | while read -r file; do
  relative_path="$(realpath --relative-to=. "$file")"
  echo "    <li><a href=\"$relative_path\">$relative_path</a></li>" >> $index_file
done

# Close the HTML tags
echo "  </ul>
</body>
</html>" >> $index_file
