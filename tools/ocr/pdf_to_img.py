import fitz
import sys

doc = fitz.open(sys.argv[1])
for i, page in enumerate(doc):
    pix = page.get_pixmap()
    pix.save(f"page_{i}.png")
