#!/usr/bin/env python3
"""
Clean watermark noise from pymupdf4llm-converted Markdown of QD-130 BYT.
Watermarks appear as scattered characters inside <br> fragments in table cells.
"""
import re
import sys

# ───────────────────────────────────────────────
# Helpers
# ───────────────────────────────────────────────

# Vietnamese characters block
VI_RE = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ'
                   r'ÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸĐ]',
                   re.IGNORECASE)

FIELD_NAME_RE = re.compile(r'^[A-Z][A-Z0-9_]+$')  # e.g. MA_LK, NGAY_SINH
DATA_TYPE_RE  = re.compile(r'^(Chuỗi|Số|Ngày|DateTime|String|Integer)$', re.IGNORECASE)
NUMBER_RE     = re.compile(r'^\d{1,4}$')           # field size e.g. 100, 15, 255

WATERMARK_TOKENS = re.compile(
    r'^[a-z0-9_/.:@ ]{1,15}$'   # short lower-ascii only = likely watermark fragment
)


def has_vietnamese(text):
    return bool(VI_RE.search(text))


def looks_like_watermark(s):
    s = s.strip()
    if not s:
        return True
    # single chars or pairs
    if len(s) <= 2 and not s.isdigit():
        return True
    # path fragments
    if re.search(r'syt_|_vt_|caobang|/\d{4}|18/0[12]|19:[0-5]', s, re.IGNORECASE):
        return True
    # short lowercase-only with _ or /
    if WATERMARK_TOKENS.match(s) and not has_vietnamese(s) and not s.isdigit():
        return True
    return False


def clean_col2_field_name(raw):
    """Column 2: keep only the ALL_CAPS field name."""
    parts = raw.split('<br>')
    for p in parts:
        p = p.strip()
        if FIELD_NAME_RE.match(p):
            return p
    # fallback: take first non-watermark
    for p in parts:
        p = p.strip()
        if p and not looks_like_watermark(p):
            return p
    return parts[0].strip()


def clean_col3_type(raw):
    """Column 3: keep only the data type keyword (Chuỗi / Số / …)."""
    parts = raw.split('<br>')
    for p in parts:
        p = p.strip()
        if DATA_TYPE_RE.match(p):
            return p
    # fallback: last non-noise token
    for p in reversed(parts):
        p = p.strip()
        if DATA_TYPE_RE.match(p.split()[0] if p else ''):
            return p.split()[0]
    # extract from combined text
    m = re.search(r'(Chuỗi|Số|Ngày)', raw)
    return m.group(1) if m else raw.split('<br>')[0].strip()


def clean_col4_size(raw):
    """Column 4: keep only the numeric field size."""
    parts = raw.split('<br>')
    for p in parts:
        p = p.strip()
        if NUMBER_RE.match(p):
            return p
    # try extracting a standalone number
    m = re.search(r'\b(\d{1,4})\b', raw)
    return m.group(1) if m else ''


def clean_col5_description(raw):
    """Column 5: description – keep all Vietnamese content, drop noise <br> fragments."""
    parts = raw.split('<br>')
    kept = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        # keep if it has Vietnamese chars OR is long enough to be real content
        if has_vietnamese(p) or len(p) > 20:
            kept.append(p)
        elif p.startswith('+') or p.startswith('-') or p.startswith('*'):
            kept.append(p)
    return '<br>'.join(kept) if kept else raw


def clean_header_row(row):
    """Fix the header row of the data table."""
    known_headers = {
        'stt': 'STT',
        'chỉ tiêu': 'Chỉ tiêu',
        'kiểu dữ': 'Kiểu dữ liệu',
        'kích thước': 'Kích thước tối đa',
        'diễn giải': 'Diễn giải',
    }
    cols = row.split('|')
    cleaned = []
    for col in cols:
        # Collapse <br> fragments
        text = ' '.join(p.strip() for p in col.split('<br>') if p.strip())
        # Remove :1, 5, trailing noise numbers
        text = re.sub(r'\s*:\d+\b', '', text)
        text = re.sub(r'\b\d+\s*$', '', text).strip()
        # Match to known header
        lower = text.lower()
        for key, val in known_headers.items():
            if key in lower:
                text = val
                break
        cleaned.append(text)
    return '|'.join(cleaned)


def clean_table_row(row):
    """Clean a regular data row (not header/separator)."""
    cols = row.split('|')
    # cols[0] is empty (leading |), cols[-1] is empty (trailing |)
    if len(cols) < 7:  # |STT|field|type|size|desc| = 7 parts
        return row

    result = [cols[0]]  # leading ''
    # col index (1-based within cols list):
    # cols[1]=STT, cols[2]=field, cols[3]=type, cols[4]=size, cols[5]=desc
    for i, col in enumerate(cols[1:-1], start=1):
        if i == 1:
            # STT – just a number, strip noise
            result.append(re.sub(r'<br>.*', '', col).strip())
        elif i == 2:
            result.append(clean_col2_field_name(col))
        elif i == 3:
            result.append(clean_col3_type(col))
        elif i == 4:
            result.append(clean_col4_size(col))
        elif i == 5:
            result.append(clean_col5_description(col))
        else:
            result.append(col)
    result.append(cols[-1])  # trailing ''
    return '|'.join(result)


# ───────────────────────────────────────────────
# Heading / body cleaning
# ───────────────────────────────────────────────

def clean_heading(line):
    """Remove trailing watermark numbers from heading lines."""
    # Remove trailing standalone digits like "130 18 01"
    line = re.sub(r'\s+\b\d{1,3}\b(\s+\b\d{1,2}\b){1,3}\s*$', '', line).rstrip()
    # Fix the banner heading with scattered blanks
    line = re.sub(r'\s{2,}', ' ', line)
    return line


def is_junk_heading(line):
    """Headings that are ONLY numbers → remove."""
    return bool(re.fullmatch(r'#{1,6}\s*[\d\s]+', line.strip()))


def clean_body_line(line):
    """Clean up a non-table, non-heading line."""
    # Remove known watermark path patterns
    line = re.sub(r'\bsyt_[^\s]+', '', line)
    line = re.sub(r'\b\d+/\d{2}/\d{4}\s+\d{2}:\d{2}:\d{2}\b', '', line)
    line = re.sub(r'\s{2,}', ' ', line)
    return line.rstrip()


# ───────────────────────────────────────────────
# Main driver
# ───────────────────────────────────────────────

def clean_markdown(md_text):
    lines = md_text.split('\n')
    output = []
    blank_run = 0
    in_table = False

    for line in lines:
        stripped = line.strip()

        # ── Table separator row ──────────────────
        if re.fullmatch(r'[|\- ]+', stripped) and '---' in stripped:
            output.append(line)
            blank_run = 0
            in_table = True
            continue

        # ── Table data row ───────────────────────
        if stripped.startswith('|') and stripped.endswith('|'):
            in_table = True
            # Detect header row (contains "Chỉ tiêu" or "Diễn giải")
            if re.search(r'(Chỉ tiêu|Diễn giải|Kiểu dữ)', stripped, re.IGNORECASE):
                output.append(clean_header_row(line))
            else:
                output.append(clean_table_row(line))
            blank_run = 0
            continue
        else:
            in_table = False

        # ── Heading line ─────────────────────────
        if stripped.startswith('#'):
            if is_junk_heading(stripped):
                continue
            output.append(clean_heading(line))
            blank_run = 0
            continue

        # ── Blank line ───────────────────────────
        if not stripped:
            blank_run += 1
            if blank_run <= 1:
                output.append('')
            continue

        # ── Regular body line ────────────────────
        blank_run = 0
        output.append(clean_body_line(line))

    return '\n'.join(output).strip() + '\n'


def post_fix(md_text):
    """Final targeted fixes after main cleaning."""
    lines = md_text.split('\n')
    out = []
    for line in lines:
        # Fix heading lines that still have scattered watermark numbers like "130 18 01"
        if line.startswith('#') and re.search(r'\b(130|18|01)\b.*\b(130|18|01)\b', line):
            line = re.sub(r'\s*/\s*\d+\s+QĐ-BYT', ' /QĐ-BYT', line)
            line = re.sub(r'(ngày\s+)/\s+/\d{4}', r'\1 / /2023', line)
            line = re.sub(r'\s+\d{1,3}\s+\d{1,2}\s+\d{1,2}\s*(g\s+)?', ' ', line)
            line = re.sub(r'\s{2,}', ' ', line).rstrip()

        # Fix table cells: field name ending with " 1" (trailing digit artifact)
        if line.startswith('|') and line.endswith('|'):
            # Remove trailing " 1" from field name column (col 2)
            line = re.sub(r'\|([A-Z][A-Z0-9_]+) \d\|', lambda m: f'|{m.group(1)}|', line)
            # Fix STT rows where field name was eaten and replaced by just "1"
            # Pattern: |16|1|Chuỗi| -> field name missing
            # These are hard to recover automatically; mark them for manual review
            line = re.sub(r'^(\|\d+\|)(1)(\|(?:Chuỗi|Số)\|)', r'\1<!-- FIELD_NAME_MISSING -->\3', line)

        out.append(line)
    return '\n'.join(out)


if __name__ == '__main__':
    import pymupdf4llm

    if len(sys.argv) < 3:
        print("Usage: clean_pdf_md.py <input.pdf> <output.md>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_md = sys.argv[2]

    print(f"Converting: {input_pdf}")
    md_text = pymupdf4llm.to_markdown(input_pdf)

    print("Cleaning watermarks and normalising ...")
    clean_md = clean_markdown(md_text)

    print("Applying final fixes ...")
    clean_md = post_fix(clean_md)

    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(clean_md)

    print(f"Done → {output_md}")
