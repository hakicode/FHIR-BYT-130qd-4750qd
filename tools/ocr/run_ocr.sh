#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <path_to_pdf>"
  exit 1
fi

PDF_PATH="$1"
PDF_DIR=$(dirname "$PDF_PATH")
PDF_NAME=$(basename "$PDF_PATH" .pdf)
OUTPUT_DIR="${PDF_DIR}/${PDF_NAME}_ocr"
VENV_PYTHON="/Users/ntkien/Library/CloudStorage/OneDrive-LACVIETCOMPUTINGCORPORATION/_PROJECT/LV FHIR EMR Gateway_Yersin/venv_pdf/bin/python3"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

mkdir -p "$OUTPUT_DIR"

echo "Converting PDF to images..."
# Tạo một file python tạm thời để chạy conversion
cat << EOF > "$OUTPUT_DIR/temp_convert.py"
import fitz
import sys
import os

pdf_path = sys.argv[1]
output_dir = sys.argv[2]
doc = fitz.open(pdf_path)

for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=300) # Tăng chất lượng ảnh
    output_path = os.path.join(output_dir, f"page_{i}.png")
    pix.save(output_path)
    print(output_path)
EOF

"$VENV_PYTHON" "$OUTPUT_DIR/temp_convert.py" "$PDF_PATH" "$OUTPUT_DIR" > "$OUTPUT_DIR/pages.list"
rm "$OUTPUT_DIR/temp_convert.py"

echo "Running OCR..."
OUTPUT_FILE="$OUTPUT_DIR/extracted_text.txt"
> "$OUTPUT_FILE"

while IFS= read -r img_path; do
    page_num=$(basename "$img_path" .png | cut -d'_' -f2)
    echo "--- Page $page_num ---" >> "$OUTPUT_FILE"
    swift "$SCRIPT_DIR/swift_ocr.swift" "$img_path" >> "$OUTPUT_FILE"
    # Dọn dẹp ảnh ngay sau khi OCR
    rm "$img_path"
done < "$OUTPUT_DIR/pages.list"

rm "$OUTPUT_DIR/pages.list"

echo "OCR completed. Result saved to: $OUTPUT_FILE"
