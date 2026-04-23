import pymupdf4llm
import sys

input_pdf = sys.argv[1]
output_md = sys.argv[2]

# Convert the PDF to markdown
md_text = pymupdf4llm.to_markdown(input_pdf)

# Save the markdown text to the specified output file
with open(output_md, "w", encoding="utf-8") as f:
    f.write(md_text)

print(f"Conversion complete. Saved to {output_md}")
