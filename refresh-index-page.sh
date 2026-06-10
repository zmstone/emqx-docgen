#!/bin/bash

index_file="index.html"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEFAULT_EMQX_REPO="$SCRIPT_DIR/tmp/emqx"
EMQX_REPO="${EMQX_REPO:-$DEFAULT_EMQX_REPO}"
EMQX_REMOTE_URL="${EMQX_REMOTE_URL:-https://github.com/emqx/emqx.git}"

# Bootstrap or repair the local EMQX clone used for release-month lookup.
# Skipped when the user pointed EMQX_REPO at their own clone.
ensure_emqx_repo() {
    if [ "$EMQX_REPO" != "$DEFAULT_EMQX_REPO" ]; then
        return 0
    fi

    # A previous run may have left a shallow / single-tag clone that can't
    # resolve historic tags. Detect that and start over.
    local shallow_marker="$EMQX_REPO/shallow"
    [ -f "$EMQX_REPO/.git/shallow" ] && shallow_marker="$EMQX_REPO/.git/shallow"
    local tag_count=0
    if [ -d "$EMQX_REPO" ]; then
        tag_count=$(git -C "$EMQX_REPO" tag --list 2>/dev/null | wc -l)
    fi
    if [ ! -d "$EMQX_REPO" ] || [ -f "$shallow_marker" ] || [ "$tag_count" -lt 50 ]; then
        echo "Bootstrapping EMQX clone at $EMQX_REPO (blobless, tags only)..." >&2
        rm -rf "$EMQX_REPO"
        mkdir -p "$(dirname "$EMQX_REPO")"
        git clone --bare --filter=tree:0 "$EMQX_REMOTE_URL" "$EMQX_REPO" >&2
    else
        # Pick up tags added since the last refresh.
        git -C "$EMQX_REPO" fetch --tags --quiet origin || true
    fi
}

ensure_emqx_repo

cd "$SCRIPT_DIR/docs"

sed -i "s/HOCON Schema Explorer/EMQX Config Schema/g" v.html

lookup_release_month() {
    file="$1"
    version="$(basename "$file" .json)"
    normalized="${version#e}"
    normalized="${normalized#v}"
    candidates=("$version" "$normalized" "v$normalized" "e$normalized")

    for tag in "${candidates[@]}"; do
        if git -C "$EMQX_REPO" rev-list -n 1 "$tag" >/dev/null 2>&1; then
            git -C "$EMQX_REPO" log -1 --format=%cd --date=format:%Y%m "$tag"
            return 0
        fi
    done

    return 1
}

format_release_month() {
    month="$1"
    if [ -n "$month" ] && [ "${#month}" -eq 6 ]; then
        printf "%s-%s" "${month:0:4}" "${month:4:2}"
    fi
}

version_sort_key() {
    file="$1"
    version="$(basename "$file" .json)"
    normalized="${version#e}"
    normalized="${normalized#v}"
    IFS='.' read -r major minor patch extra <<< "$normalized"
    major="${major:-0}"
    minor="${minor:-0}"
    patch="${patch:-0}"
    printf "%05d%05d%05d|%s" "$major" "$minor" "$patch" "$version"
}

gen_lang_rows() {
    lang="$1"
    # Find all JSON files in the subdirectories and sort in reverse version order
    find "$lang" -type f -iname "*.json" | grep -v -E "$lang/[v|e]" | sort -r --version-sort | while read -r file; do
        month="$(lookup_release_month "$file" || true)"
        month_display="$(format_release_month "$month")"
        version_key="$(version_sort_key "$file")"
        echo "<div class=\"row\" data-version-key=\"$version_key\" data-month-key=\"$month\"><div class=\"cell version-cell\"><a href=\"v.html?s=$file\">$file</a></div><div class=\"cell month-cell\">${month_display}</div></div>"
    done
    find "$lang" -type f -iname "e*.json" | sort -r --version-sort | while read -r file; do
        month="$(lookup_release_month "$file" || true)"
        month_display="$(format_release_month "$month")"
        version_key="$(version_sort_key "$file")"
        echo "<div class=\"row\" data-version-key=\"$version_key\" data-month-key=\"$month\"><div class=\"cell version-cell\"><a href=\"v.html?s=$file\">$file</a></div><div class=\"cell month-cell\">${month_display}</div></div>"
    done
}

EN_LIST_ENTERPRISE="$(gen_lang_rows en)"
ZH_LIST_ENTERPRISE="$(gen_lang_rows zh)"

replace_section() {
    start_marker="$1"
    end_marker="$2"
    replacement="$3"
    tmp_file="$(mktemp)"
    printf '%s\n' "$replacement" > "$tmp_file"
    START_MARKER="$start_marker" END_MARKER="$end_marker" REPLACEMENT_FILE="$tmp_file" perl -0pi -e '
        my $start = $ENV{START_MARKER};
        my $end = $ENV{END_MARKER};
        my $file = $ENV{REPLACEMENT_FILE};
        open my $fh, "<", $file or die "failed to open replacement file: $!";
        local $/;
        my $replacement = <$fh>;
        close $fh;
        s{([ \t]*\Q$start\E\n).*?(\n[ \t]*\Q$end\E)}{$1 . $replacement . $2}se
            or die "failed to replace section between $start and $end";
    ' "$index_file"
    rm -f "$tmp_file"
}

replace_section "<!-- BEGIN EN_ROWS -->" "<!-- END EN_ROWS -->" "$EN_LIST_ENTERPRISE"
replace_section "<!-- BEGIN ZH_ROWS -->" "<!-- END ZH_ROWS -->" "$ZH_LIST_ENTERPRISE"
