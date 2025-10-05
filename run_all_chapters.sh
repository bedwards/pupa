#!/usr/bin/env bash
set -euxo pipefail

# Root of your project and Python entrypoint.
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="$PROJECT_DIR/pupa_04.py"

# Source and destination. Adjust if you relocate data.
BOOK_DIR="${PROJECT_DIR}/../pupa_data/Zhang Henshui - The Story of a Noble Family"
SRC_DIR="${BOOK_DIR}/chapters_chinese"
DST_DIR="${BOOK_DIR}/chapters_english_01"

# Make sure things exist.
test -x "$(command -v python)"
test -f "$PY"
test -d "$SRC_DIR"
mkdir -p "$DST_DIR"

# Process files in a stable, numeric-aware order.
# This will naturally do 000_prologue.txt before 001_chapter.txt, etc.
# If pupa_04.py is idempotent, we can skip chapters with an existing output.
# Adjust the OUT mapping if your script writes a different filename.
LC_ALL=C find "$SRC_DIR" -type f -name '*.txt' -print0 \
| sort -z \
| while IFS= read -r -d '' INPATH; do
  base="$(basename "$INPATH")"
  OUTPATH="${DST_DIR}/${base}"

  # Skip if a non-empty output file already exists.
  if [[ -s "$OUTPATH" ]]; then
    echo "Skipping already-translated: $base"
    continue
  fi

  echo "Translating: $base"
  python "$PY" "$INPATH"

  # Optional: sanity check that something was created.
  # Comment this block out if pupa_04.py writes a different path.
  if [[ ! -s "$OUTPATH" ]]; then
    echo "Expected output not found or empty: $OUTPATH" >&2
    exit 1
  fi
done

echo "All done."
