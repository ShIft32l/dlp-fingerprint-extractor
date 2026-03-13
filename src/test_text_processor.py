"""Quick test for text_processor module."""
import sys
sys.path.insert(0, "src")

from text_processor import clean_text, split_into_sentences, extract_long_phrases

# ----- Test 1: clean_text strips junk & boilerplate -----
messy = """
   Page 1 of 10

   This is a   paragraph  with   extra   spaces.

   \x00Hidden\x07 control \x0b chars here.

   _______________
   Regards,

   12/03/2026

   The board approved the acquisition of the target company for a total of $5.2 million.

   - 3 -

   Trân trọng,
"""

cleaned = clean_text(messy)
print("=== CLEANED TEXT ===")
print(repr(cleaned))
print()

assert "Page 1 of 10" not in cleaned, "Boilerplate page number not removed"
assert "Regards," not in cleaned, "Signature not removed"
assert "Trân trọng," not in cleaned, "Vietnamese signature not removed"
assert "___" not in cleaned, "Separator not removed"
assert "- 3 -" not in cleaned, "Page number variant not removed"
assert "\x00" not in cleaned, "Control chars not removed"
assert "  " not in cleaned, "Double spaces not collapsed"
assert "board approved" in cleaned, "Real content was wrongly removed"
print("✅ Test 1 PASSED: clean_text works correctly\n")

# ----- Test 2: extract_long_phrases filters short sentences -----
raw = """
Board Meeting Minutes. Date: January 15, 2026.

The Chief Financial Officer presented the quarterly financial report showing revenue growth of 15% year-over-year.
The board unanimously approved the proposed budget allocation for the next fiscal year.
Báo cáo:
Trân trọng,
OK.
Yes.
The committee recommends conducting a comprehensive security audit of all customer-facing applications.
"""

candidates = extract_long_phrases(raw, min_tokens=6)
print("=== CANDIDATES ===")
for i, c in enumerate(candidates, 1):
    print(f"  {i}. {c}")
print()

# Short fragments should be gone
for short in ["Báo cáo:", "OK.", "Yes."]:
    assert short not in candidates, f"Short phrase '{short}' should have been filtered"

assert len(candidates) >= 3, f"Expected >=3 candidates, got {len(candidates)}"
print(f"✅ Test 2 PASSED: extract_long_phrases returned {len(candidates)} candidates\n")

print("🎉 All text_processor tests passed!")
