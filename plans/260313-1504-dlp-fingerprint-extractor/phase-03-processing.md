# Phase 03: Text Processing & Chunking
Status: ✅ Complete

## Objective
Tiếp nhận chuỗi văn bản mộc (Raw Text) từ Parser, làm sạch và chia nhỏ văn bản thành các câu/cụm từ dài (N-grams hoặc Segments) hợp lệ để gửi cho AI.

## Requirements
### Functional
- [ ] Hàm `clean_text(raw_text)` loại bỏ các ký tự rác ẩn, chuẩn hóa khoảng trắng.
- [ ] Hàm `extract_long_phrases(text, min_tokens=6)` sử dụng NLTK/Spacy hoặc regex nâng cao để tách câu và chỉ giữ các câu có độ dài > 5 từ (tokens).
- [ ] Loại bỏ các câu quá phổ thông/Stop words nếu cần thiết (để giảm chi phí gọi API API Gemini).

## Implementation Steps
1. [ ] Cài đặt gói ngôn ngữ Spacy/NLTK nếu cần.
2. [ ] Viết hàm `clean_text` vào `src/text_processor.py`.
3. [ ] Chạy Regex loại bỏ header/footer/chữ ký (những chuỗi lặp lại vô nghĩa).
4. [ ] Viết hàm `split_into_sentences` tách văn bản thành list các câu (sentence boundary detection).
5. [ ] Lọc bỏ các câu < 5 từ và mảng Array trả về chứa các đoạn văn bản tiềm năng (Candidates).

## Files to Create/Modify
- `src/text_processor.py`

## Test Criteria
- [ ] Bỏ 1 đoạn text lộn xộn vào, hàm `clean` trả về đoạn text rõ ràng.
- [ ] Hàm `extract_long_phrases` loại bỏ hoàn toàn các câu siêu ngắn như "Trân trọng," hoặc "Báo cáo:".

---
Next Phase: phase-04-ai-evaluator.md
