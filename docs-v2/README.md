# reformatted schema dump from files in docs/{en,zh}

The files are generated with bash script as below:
Working dir must be emqx.git repo with both `emqx` and `emqx-enterprise` profile compiled already.
The escript named `scripts/schema-dump-reformat.escript` was added in this PR: https://github.com/emqx/emqx/pull/11970

```
#!/bin/bash

set -euo pipefail

DIR='~/src/emqx/emqx-docgen'
OUTDIR="$DIR/docs-v2"
FILES=$(find "$DIR"/docs/{en,zh} -name '*.json')

for f in $FILES; do
    name=$(basename $f)
    lang=$(basename $(dirname "$f"))
    case $name in
        v*)
            export PROFILE=emqx
            ;;
        e*)
            export PROFILE=emqx-enterprise
            ;;
    esac
    mkdir -p "$OUTDIR/$lang"
    outfile="$OUTDIR/$lang/$name"
    echo $f
    ./scripts/schema-dump-reformat.escript $f | jq -M --sort-keys . > "$outfile"
done
```
