#!/usr/bin/env python3

"""Standalone OCR watermark cleanup rule.

This file mirrors the post-OCR cleanup logic used by `run_ocr.sh` so the
rule can be reviewed or compared before it is used in a workflow.
"""

import re
import sys


timestamp_pattern = re.compile(r'^\s*(?:\d{2}/\d{4}\s+\d{2}:\d{2}:\d{2}|\d{4}\s+\d{2}:\d{2})\s*$')

# Watermark cleanup runs after OCR completes.
# This is a generic post-processing rule for OCR output: strip known watermark
# fragments from the extracted text, then drop lines that become empty or still
# look like watermark noise.
watermark_fragment_patterns = [
  re.compile(r'(?i)syt[_\s-]*caob[a-z]{0,8}'),
  re.compile(r'(?i)\bcaob[a-z]{0,8}\b'),
  re.compile(r'(?i)_vt_'),
  re.compile(r'(?i)\bpang\s*thi\s*da\b'),
  re.compile(r'(?i)\bhoang(?:\s+thi\s+da|\s+th\s+da)?\b'),
]


def strip_watermark_fragments(text):
  cleaned = text
  for pattern in watermark_fragment_patterns:
    cleaned = pattern.sub(' ', cleaned)
  cleaned = re.sub(r'[\s_\-.,;:/\\]+', ' ', cleaned)
  cleaned = re.sub(r'\s{2,}', ' ', cleaned).strip()
  return cleaned


def looks_like_watermark_line(text):
  normalized = text.strip().lower()
  if not normalized:
    return False

  if any(pattern.search(normalized) for pattern in watermark_fragment_patterns):
    if len(normalized) <= 80:
      return True

    stripped = strip_watermark_fragments(normalized)
    if not stripped:
      return True

    alnum_count = len(re.findall(r'[\wÀ-ỹ]', stripped))
    return alnum_count <= 3

  return False


def clean_output_file(output_file):
  with open(output_file, 'r', encoding='utf-8') as handle:
    lines = handle.readlines()

  cleaned_lines = []
  blank_run = 0
  for line in lines:
    stripped = line.strip()
    if not stripped:
      blank_run += 1
      if cleaned_lines and blank_run <= 1:
        cleaned_lines.append(line)
      continue

    blank_run = 0
    if stripped.startswith('--- Page ') and stripped.endswith('---'):
      cleaned_lines.append(line)
      continue
    if timestamp_pattern.match(stripped):
      continue
    if looks_like_watermark_line(stripped):
      continue

    cleaned = strip_watermark_fragments(stripped)
    if cleaned:
      cleaned_lines.append(cleaned + '\n')

  with open(output_file, 'w', encoding='utf-8') as handle:
    handle.writelines(cleaned_lines)


if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Usage: watermark_cleanup_rule.py <extracted_text.txt>')
    sys.exit(1)

  clean_output_file(sys.argv[1])
