#!/usr/bin/env bash
# Build the CS-AML specification release package (DOCX + PDF) from canonical Markdown.
#
# Usage: tools/release/build_release.sh <version> [git-ref]
#   e.g. tools/release/build_release.sh 0.1.4 v0.1.4-spec
#
# Requirements on the build host: git, docker (no root needed if the user is in the docker group).
# The source documents are taken from <git-ref> (default v<version>-spec) via `git archive`, so the
# package reflects the tagged baseline even if the working tree has moved on. The release tooling
# itself (this directory) is taken from the working tree.
# Output: release/v<version>/ (replaced if it exists). Build logs: $WORK (printed at the end; removed
# unless KEEP_WORK=1).
set -euo pipefail

version="${1:?usage: build_release.sh <version> [git-ref]}"
ref="${2:-v${version}-spec}"
here="$(cd "$(dirname "$0")" && pwd)"
repo="$(git -C "$here" rev-parse --show-toplevel)"
image="csaml-specbuild:pandoc-3.10.0.0"
commit="$(git -C "$repo" rev-parse "${ref}^{commit}")"
epoch="$(git -C "$repo" log -1 --format=%ct "$commit")"

work="$(mktemp -d "${TMPDIR:-/tmp}/csaml-release.XXXXXX")"
trap '[ "${KEEP_WORK:-0}" = 1 ] || rm -rf "$work"' EXIT
mkdir -p "$work/src" "$work/out" "$work/build"
git -C "$repo" archive "$commit" Documents contracts schemas | tar -x -C "$work/src"
cp -r "$here" "$work/tools"

docker build -q -t "$image" "$here" >/dev/null
docker run --rm --network none -u "$(id -u):$(id -g)" \
  -e HOME=/tmp -e SOURCE_DATE_EPOCH="$epoch" -e FORCE_SOURCE_DATE=1 -e ONLY="${ONLY:-}" \
  -v "$work:/work" -w /work "$image" \
  python3 /work/tools/release.py --version "$version" --src /work/src --out /work/out \
    --work /work/build --ref "$ref" --commit "$commit"

dest="$repo/release/v${version}"
rm -rf "$dest"
mkdir -p "$(dirname "$dest")"
cp -r "$work/out" "$dest"
cp "$work/build/qa.txt" "$work/qa.txt"
echo "Release package written to $dest ($(du -sh "$dest" | cut -f1))"
echo "QA summary:"; cat "$work/qa.txt"
