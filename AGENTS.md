# Agent guide: adding a new EMQX version

This repo holds, per EMQX release, the schema dump (`docs/{en,zh}/<version>.json`,
`docs-v2/{en,zh}/<version>.json`) and the HOCON examples
(`docs/examples/<version>/*.hocon`).

Adding a release is two independent steps: **build the schema**, then **generate
the examples**. They are usually two commits.

Version strings follow the git tag. v5 tags carry an `e` prefix (`e5.10.4`); v6
and later tags do not (`6.3.0`, not `e6.3.0`).

**v5 naming is not uniform across the repo.** The schema JSON keeps the `e`
prefix, the examples directory drops it, and `-b` takes the bare version:

| | v5 | v6+ |
|---|---|---|
| `./gen` argument | `e5.10.5` | `6.3.1` |
| schema file | `docs/en/e5.10.5.json` | `docs/en/6.3.1.json` |
| examples dir | `docs/examples/5.10.5/` | `docs/examples/6.3.1/` |
| `-b` base | `-b 5.10.4` | `-b 6.3.0` |

`generate-examples.py` derives the examples directory as `schema_path.stem.lstrip("ve")`,
and resolves `-b` against `{v}.json`, `v{v}.json` and `e{v}.json` in turn.

## Step 1 — build the schema

```bash
./gen <version> --rebuild
```

This clones the tag into `tmp/emqx`, runs `make` inside the builder image, and
copies four JSON files into `docs/` and `docs-v2/`. It also refreshes
`docs/index.html`. Takes tens of minutes.

**Before running it, add a `BUILDER` case for the new minor** in `gen` — the
`case "$VERSION"` block near the top. Without a matching case the script falls
back to an old default builder (OTP 27) and the build fails or produces a wrong
schema. Find the right image from the release tag:

```bash
cd /mnt/data/emqx/63 && git fetch --tags origin <version>
git show <version>:.tool-versions                        # erlang + elixir versions
git grep -h -A3 builder_vsn <version> -- '.github/workflows/*.yaml' | grep default
```

The image is `ghcr.io/emqx/emqx-builder/<builder_vsn>:<elixir>-<erlang>-ubuntu22.04`.
Confirm it exists before starting the build:

```bash
docker manifest inspect ghcr.io/emqx/emqx-builder/6.1-8:1.19.1-28.4.1-4-ubuntu22.04
```

Commit as `Add <version>` — the four JSON files plus `docs/index.html`.

## Step 2 — generate the examples (no OpenAI key)

`generate-examples.py` normally calls OpenAI. Without a key, use its
`--save-requests` dry-run mode and fill in the payloads by hand. The script only
ever touches schemas that actually changed; everything else is copied forward
from the base version.

Base version = the previous release in the same directory listing (e.g. base
`6.2.3` for `6.3.0`).

```bash
# 1. See what changed.
python3 ./generate-examples.py --list-changes -b <base> ./docs/en/<version>.json

# 2. Copy unchanged examples forward; write one request payload per
#    changed/new schema to ./requests. OpenAI is NOT called.
python3 ./generate-examples.py --save-requests ./requests -b <base> ./docs/en/<version>.json
```

### 2a. Split "changed" into cosmetic vs example-affecting

Most "changed" schemas do not need a new example. Description edits, type
refinements (`integer()` → `pos_integer()`), and reordering of map fields or
union members do not change the rendered HOCON — for those, just
`cp docs/examples/<base>/<file> docs/examples/<version>/`.

Run this to classify every changed schema at field level, so you only hand-write
the ones that matter:

```bash
python3 - <<'EOF'
import json, importlib.util, difflib
spec = importlib.util.spec_from_file_location("ge", "generate-examples.py")
ge = importlib.util.module_from_spec(spec); spec.loader.exec_module(ge)

BASE, NEW = 'docs/en/<base>.json', 'docs/en/<version>.json'
bl = ge.build_schema_lookup(ge.load_schema(BASE))
nl = ge.build_schema_lookup(ge.load_schema(NEW))

for name, n in nl.items():
    b = bl.get(name)
    if b is None or ge.structs_are_equal(ge.slim_struct(b), ge.slim_struct(n)):
        continue
    bm = {f['name']: f for f in ge.slim_struct(b).get('fields', [])}
    nm = {f['name']: f for f in ge.slim_struct(n).get('fields', [])}
    added, removed = [k for k in nm if k not in bm], [k for k in bm if k not in nm]
    print(f"=== {name}")
    if added: print("  ADDED:", added)
    if removed: print("  REMOVED:", removed)
    for k in nm:
        if k in bm and bm[k] != nm[k]:
            d = {kk: (bm[k].get(kk), nm[k].get(kk)) for kk in set(bm[k]) | set(nm[k])
                 if bm[k].get(kk) != nm[k].get(kk)}
            print(f"  MOD {k}: {json.dumps(d, default=str)[:300]}")
EOF
```

A struct that prints only `MOD <field>: {"desc": ...}` is cosmetic — copy it.
A struct that prints nothing under its `===` header changed only in `paths` or
in member *order*; also cosmetic. Confirm order-only changes by comparing the
field-name sets and union-member name sets — if `added` and `removed` are both
empty, nothing rendered changes.

Only `ADDED` / `REMOVED` fields, changed `default` / `raw_default`, and new
sub-structs need an edited example.

### 2b. Edit the affected examples

Edit rules (from the payload's system prompt in `requests/<struct>.json`):

- HOCON syntax, `=` delimiters, 2-space indentation.
- Use each field's `default` / `raw_default` as the value; quote byte and
  duration values (`"30s"`, `"10MB"`).
- Skip fields whose `desc` starts with `Deprecated`, and skip `tag` /
  `description` on bridge, action, and connector structs.
- Sub-structs and union-of-struct members render as placeholder comments:
  `#substruct(namespace:struct_name)`, one line per union member.
- Insert a new field at its schema position — read the field order from the
  payload:
  ```bash
  python3 -c "
  import json; p=json.load(open('requests/<struct>.json'))
  s=json.loads(p['input'][1]['content'].split('schema:\n',1)[1])
  print([f['name'] for f in s['fields']])"
  ```
- Filename is the struct `full_name` with `:` replaced by `-`
  (`emqx:ssl_client_opts` → `emqx-ssl_client_opts.hocon`).
- For a brand-new struct, expand its first `paths` entry: `$NAME` becomes a
  sample key, `$INDEX` becomes `= [` with the element indented on a new line.
  Copy the shape from an existing sibling (e.g. `connector_http-request.hocon`).

When one field is added to many structs, a `sed` insert after a stable anchor
line is faster and less error-prone than editing each file:

```bash
cd docs/examples
for f in emqx-mqtt_tcp_listener emqx-mqtt_ssl_listener; do
  sed 's/^  enable_authn = true$/  enable_authn = true\n  allow_log_packet_data_from = ""/' \
    <base>/$f.hocon > <version>/$f.hocon
done
```

### 2c. Verify, then clean up

Both checks must pass before committing:

```bash
python3 - <<'EOF'
import json, os, re
V, B = '<version>', 'docs/examples/<version>'
names = {s['full_name'] for s in json.load(open(f'docs/en/{V}.json'))} - {'emqx:Root Config Keys'}
files = {f[:-6] for f in os.listdir(B) if f.endswith('.hocon')}
expected = {n.replace(':', '-') for n in names}
print('missing:', sorted(expected - files))
print('extra:  ', sorted(files - expected))
bad = [(f, m) for f in os.listdir(B)
       for m in re.findall(r'#substruct\(([^)]+)\)', open(f'{B}/{f}').read())
       if m.replace(':', '-') not in files]
print('unresolved placeholders:', bad)
EOF
```

- One `.hocon` per struct, root excluded — file count equals struct count minus 1.
- Every `#substruct(...)` resolves to a file in the same version directory.

An unresolved placeholder is often inherited, not new: the copy-forward carries a
bad example from the base version unchanged. Check before you edit —
`diff docs/examples/<base>/<file> docs/examples/<version>/<file>`. When the files
are identical, the defect predates this release. Fix it in the new version only;
leave already-released directories as the record of what shipped. Check how the
other major line renders the same struct, which is often already correct.

Two such defects were found and fixed in 5.10.5:
`emqx-log.hocon` referenced `#substruct(emqx:handler_name)`, but `emqx:log.file`
is a union of `emqx:log_file_handler` and a *map* named `handler_name` whose
values are that same struct; there is no `emqx:handler_name` struct.
`cluster-link.hocon` rendered `password` as `#substruct(emqx_schema_secret:secret())`,
but the field is a primitive and takes a quoted string.

Then `rm -rf requests` (scratch, regenerable) and commit as
`Add examples <version>`.

## Effort reference

| Round | Flagged | Cosmetic (copied) | Edited | New structs |
|---|---|---|---|---|
| 6.2.2 → 6.2.3 | 37 | 15 | 20 | 2 |
| 6.3.0 → 6.3.1 (patch) | 12 | 10 | 2 | 0 |
| 5.10.4 → 5.10.5 (patch) | 22 | 18 | 4 | 0 |
| 6.2.3 → 6.3.0 (minor) | 88 | 17 | 52 | 18 |

A patch release is usually an hour of work; a minor release is where the
classification script in 2a earns its keep. Most flagged schemas are cosmetic.
A union whose members were only reordered is cosmetic too, as long as the value
the example already picks is still a member — check that rather than assuming.

Two releases can be built in one run, but only sequentially: `gen` uses a fixed
container name (`docgen`) and one shared `tmp/emqx` clone that `--rebuild` wipes.
