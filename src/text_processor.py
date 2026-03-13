"""
Text Processing & Chunking Module
- Cleans raw text extracted from documents
- Splits text into sentences
- Filters and returns only long, meaningful phrases (candidates for fingerprinting)
"""

import re
import logging
from typing import List, Dict

import nltk

# Ensure punkt tokenizer data is available
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", quiet=True)

from nltk.tokenize import sent_tokenize

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Common boilerplate patterns to strip (headers, footers, signatures, etc.)
# ---------------------------------------------------------------------------
_BOILERPLATE_PATTERNS: List[str] = [
    # Page numbers: "Page 1 of 10", "- 1 -", "1 | Page"
    r"(?i)page\s+\d+\s+of\s+\d+",
    r"^\s*-\s*\d+\s*-\s*$",
    r"^\s*\d+\s*\|\s*page\s*$",
    # Common email / letter footers
    r"(?i)^(regards|sincerely|cheers|best wishes|trân trọng|thân mến),?\s*$",
    # Repeated dashes / underscores / equals used as separators
    r"^[\-_=]{3,}$",
    # Standalone dates  (e.g. "12/03/2026")
    r"^\s*\d{1,2}[/\-\.]\d{1,2}[/\-\.]\d{2,4}\s*$",
]

_COMPILED_BOILERPLATE = [re.compile(p, re.MULTILINE) for p in _BOILERPLATE_PATTERNS]


def clean_text(raw_text: str) -> str:
    """
    Clean raw extracted text:
    - Strip invisible / control characters
    - Normalise whitespace (multiple spaces → one, multiple newlines → two)
    - Remove common boilerplate lines (headers, footers, signatures)
    """
    if not raw_text:
        return ""

    text = raw_text

    # 1. Remove common Unicode control / zero-width characters
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f\u200b-\u200d\ufeff]", "", text)

    # 2. Remove boilerplate lines
    lines = text.split("\n")
    cleaned_lines: List[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            cleaned_lines.append("")
            continue
        is_boilerplate = False
        for pattern in _COMPILED_BOILERPLATE:
            if pattern.search(stripped):
                is_boilerplate = True
                break
        if not is_boilerplate:
            cleaned_lines.append(stripped)
    text = "\n".join(cleaned_lines)

    # 3. Collapse multiple blank lines into a single blank line
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 4. Collapse multiple spaces into one
    text = re.sub(r"[ \t]{2,}", " ", text)

    return text.strip()


def split_into_sentences(text: str) -> List[str]:
    """
    Split cleaned text into a list of sentences using NLTK's sent_tokenize.
    Returns sentences with leading/trailing whitespace stripped.
    """
    if not text:
        return []

    sentences = sent_tokenize(text)
    return [s.strip() for s in sentences if s.strip()]


def extract_long_phrases(text: str, min_tokens: int = 6) -> Dict[str, int]:
    """
    Full pipeline:
    1. Clean text
    2. Split into sentences
    3. Keep only sentences with >= min_tokens words

    Returns a dictionary of deduplicated candidate phrases mapped to their occurrence count.
    Note: The dictionary keys are the actual original phrases (first seen case), and values are counts.
    """
    cleaned = clean_text(text)
    sentences = split_into_sentences(cleaned)

    # We map formatted key -> (original phrase, count) to preserve actual casing
    seen_map = {}
    for sentence in sentences:
        token_count = len(sentence.split())
        if token_count >= min_tokens:
            key = sentence.lower()
            if key not in seen_map:
                seen_map[key] = {"phrase": sentence, "count": 1}
            else:
                seen_map[key]["count"] += 1

    # Extract the final formatted result
    candidates_counts: Dict[str, int] = {}
    for entry in seen_map.values():
         candidates_counts[entry["phrase"]] = entry["count"]

    logger.info(
        "extract_long_phrases: %d sentences → %d candidates (min_tokens=%d)",
        len(sentences),
        len(candidates_counts),
        min_tokens,
    )
    return candidates_counts
