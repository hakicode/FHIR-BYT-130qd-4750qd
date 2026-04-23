# OCR Pipeline

This directory contains tools to convert every PDF page into images first, then run OCR to extract text using macOS's built-in Vision framework.
The workflow applies to all PDF files, including scanned PDFs and PDFs that already contain selectable text.

## Requirements

1. **Python Virtual Environment (`venv_pdf`)**: Needs to exist in the project root with `PyMuPDF` installed.
   - If not present, run: `python3 -m venv venv_pdf && source venv_pdf/bin/activate && pip install PyMuPDF`
2. **macOS Environment**: The text extraction relies on the `swift` command and the macOS Vision framework.

## Usage

You can use the wrapper script `run_ocr.sh` to extract text from a PDF. It always rasterizes the PDF into page images first, then runs OCR, and finally cleans up the temporary images afterwards.

```bash
cd tools/ocr
./run_ocr.sh "/path/to/your/document.pdf"
```

### What it does:

1. Creates an output directory named `[pdf_name]_ocr` alongside the original PDF.
2. Converts every page of the PDF to a high-resolution PNG image, regardless of whether the PDF already has a text layer.
3. Uses the `swift_ocr.swift` script to perform OCR on each image using macOS's Vision API (specifically configured for Vietnamese `vi-VN`).
4. Appends the raw OCR text into `[pdf_name]_ocr/extracted_text.txt`.
5. Cleans up the temporary PNG images automatically to save space.

### Watermark cleanup rule

Watermark removal is no longer part of the main wrapper script. If you want to compare or apply that rule separately, use [watermark_cleanup_rule.py](watermark_cleanup_rule.py) as the standalone reference copy.

## Files

- `run_ocr.sh`: The main bash wrapper script to execute the pipeline.
- `swift_ocr.swift`: The Swift script that invokes the Vision API for OCR on a single image.
- `watermark_cleanup_rule.py`: Standalone reference copy of the post-OCR watermark cleanup rule.
- `pdf_to_img.py`: (Deprecated/Backup) A simple script to convert PDF to images manually. The wrapper script now does this internally with higher resolution.
