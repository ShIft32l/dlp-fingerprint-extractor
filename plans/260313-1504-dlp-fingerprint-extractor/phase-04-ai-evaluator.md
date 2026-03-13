# Phase 04: AI Evaluation Engine (Gemini)
Status: ✅ Complete

## Objective
Gửi các câu/cụm từ văn bản được trích xuất (từ Phase 3) sang cho Gemini AI chấm điểm qua API, lấy lại một danh sách chỉ chứa những Fingerprints "đặc thù nhất" của tài liệu.

## Requirements
### Functional
- [ ] Tích hợp Google Gemini API qua thư viện `google-generativeai`.
- [ ] Xây dựng Prompt Engineering chuyên biệt để nhận diện "Corporate Specific Phrases" cho DLP.
- [ ] Tính năng Rate Limiter (ngủ/chờ giữa các request API) tránh bị block do giới hạn quota.
- [ ] Gửi Text theo Mảng (Batch Processing/Chunking) tiết kiệm số lần gọi API thay vì gửi từng dòng một.

## Implementation Steps
1. [ ] Cấu hình Gemini model (VD: `gemini-1.5-flash` hoặc `gemini-1.5-pro` tùy độ phức tạp).
2. [ ] Thiết kế *System Prompt* (Định hướng cho AI: "Mày là một chuyên gia DLP, phân tích danh sách câu này...").
3. [ ] Viết hàm `evaluate_phrases_batch(phrases_list)` trong `src/ai_evaluator.py`.
4. [ ] Nhận kết quả từ AI (Yêu cầu AI trả về chuẩn JSON List).
5. [ ] Try/Catch xử lý lỗi kết nối mạng hoặc lỗi quota (429 Too Many Requests).

## Files to Create/Modify
- `src/ai_evaluator.py`

## Test Criteria
- [ ] Gửi một test List: `["Xin chào bạn", "Cấu trúc mạng SD-WAN chi nhánh HCM", "Trân trọng cảm ơn"]`.
- [ ] AI trả về đúng CHỈ DUY NHẤT câu `"Cấu trúc mạng SD-WAN chi nhánh HCM"`.
- [ ] API trả về Output là 1 mảng JSON/Python List hợp lệ chứ không bị vỡ format.

---
Next Phase: phase-05-generator.md
