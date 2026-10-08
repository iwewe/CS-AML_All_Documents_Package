#!/usr/bin/env bash
# Regenerate full Markdown from the v0.1 DOCX baseline (requires pandoc >= 3).
# Usage: tools/docx2md/convert.sh <output-dir>
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
out="${1:?output dir}"
tmp="$(mktemp -d)"
mkdir -p "$out"
for f in "$here"/../../Documents/*.docx; do
  name="$(basename "$f" .docx)"
  python3 "$here/prep.py" "$f" "$tmp/$name.docx"
  pandoc -f docx+styles "$tmp/$name.docx" -t gfm --wrap=none --lua-filter="$here/tables.lua" -o "$out/$name.md"
  sed -i 's/\\`/`/g' "$out/$name.md"
done
rm -rf "$tmp"
