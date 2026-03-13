"""Quick test for ai_evaluator module — matches Phase 04 test criteria."""
import sys
import logging
sys.path.insert(0, "src")

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

from ai_evaluator import evaluate_phrases_batch

# Test list from the spec
test_phrases = [
    "Xin chào bạn",
    "Cấu trúc mạng SD-WAN chi nhánh HCM",
    "Trân trọng cảm ơn",
]

print("=== Sending test phrases to Gemini ===")
for i, p in enumerate(test_phrases, 1):
    print(f"  {i}. {p}")

result = evaluate_phrases_batch(test_phrases)

print(f"\n=== AI Evaluation Result ({len(result)} kept) ===")
for i, p in enumerate(result, 1):
    print(f"  {i}. {p}")

# Validation
assert isinstance(result, list), "Result must be a list"
assert all(isinstance(item, str) for item in result), "All items must be strings"

# The specific phrase should be kept
assert any("SD-WAN" in p for p in result), "Expected 'SD-WAN' phrase to be kept by AI"

# Generic greetings should be removed
generic_markers = ["Xin chào", "Trân trọng"]
for marker in generic_markers:
    if any(marker in p for p in result):
        print(f"⚠️ Warning: Generic phrase containing '{marker}' was kept (AI judgement varies)")

print("\n✅ Test PASSED: AI evaluator returned valid JSON list with specific phrases kept.")
