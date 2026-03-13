# Phase 06: Testing & Refinement
Status: ⬜ Pending

## Objective
Kiểm thử toàn bộ hệ thống để đảm bảo kết quả chuỗi Fingerprints xuất ra thực sự tốt, đúng format và code xử lý được đa dạng các file bị lỗi hoặc vỡ layout without crashing.

## Requirements
### Functional
- [ ] Chạy Test qua Thư mục `samples/test_batch_1/` chứa ít nhất 3 loại file: `PDF`, `DOCX`, `TXT`.
- [ ] Đảm bảo các đoạn Text được filter là Hữu ích cho quá trình phân tích của Google Gemini.

## Implementation Steps
1. [ ] Tạo một File `REQUIREMENTS_TESTING.md` ghi nhận Prompt cho Google Gemini.
2. [ ] Tạo 3 file Test (Dummy Docs) về "Quy định bảo mật của công ty ABC".
3. [ ] Chạy lệnh qua CLI command: `python main.py --input ./samples/test_batch_1 --type "Security_Policy"`
4. [ ] Mở kết quả Output và đánh giá bằng tay (Reviewing) xem các câu được AI chọn có mang tính "Fingerprint" hay không (Có keyword, có cấu trúc ngữ nghĩa dài).
5. [ ] Thực hiện Tinh chỉnh lại file `src/ai_evaluator.py` nếu kết quả chưa đạt bằng việc **Tối ưu Prompt (System Prompt Engineering)**.
6. [ ] Kiểm tra cơ chế giới hạn Token Limit nếu gửi văn bản quá dài với Gemini (Ví dụ 1 file 50 trang). Cần thiết lập chế độ Rate Limit backoff.

## Files to Create/Modify
- `samples/` - Thư mục giả định chứa File.
- Các logs sinh ra trong thư mục `logs/` để debug lỗi.

## Test Criteria
- [ ] Script không chết giữa chừng do file PDF lỗi font chữ mã hóa.
- [ ] Tổng số requests gửi đến Gemini API xấp xỉ đúng số câu thỏa mãn điều kiện dài >5 tokens thay vì gửi cả đoạn văn rác.
- [ ] Tỷ lệ False-Positive giảm so với chỉ bóc tách Keyword như trước đây (User manual testing).

---
Next Phase: Hoàn thành Project.
