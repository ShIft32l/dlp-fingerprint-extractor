# Requirements: Testing & AI Prompt Engineering

DLP Fingerprint Extractor sử dụng AI (Gemini) để lọc các cụm từ quan trọng. Tài liệu này ghi nhận các tiêu chuẩn và tham số sử dụng trong quá trình kiểm thử.

## 1. Tiêu chuẩn đánh giá Fingerprint

Một cụm từ được coi là "Chất lượng cao" (High Quality) nếu:
- **Độ dài**: Có ít nhất 6-10 tokens (để tránh trùng lặp ngẫu nhiên).
- **Tính đặc thù**: Chứa các tên riêng, mã dự án, hoặc cấu trúc câu mang tính chuyên môn cao.
- **Tính ổn định**: Không chứa các thông tin thay đổi quá nhanh (như thời gian cụ thể đến từng giây).

## 2. Chiến lược Prompt Engineering

### System Instruction (Hiện tại)
AI được chỉ thị đóng vai trò là "DLP Analyst".
- **Keep**: Proper nouns, project names, proprietary processes, financial figures.
- **Discard**: Greetings, common business language, page numbers, formatting junk.

### Cần tinh chỉnh (Refinement Goals)
- [ ] Tăng cường việc nhận diện các mã dự án dạng viết tắt (Nhiều khi AI coi là rác).
- [ ] Cải thiện việc xử lý các bảng biểu (Tables) bị vỡ layout khi trích xuất từ PDF.

## 3. Kịch bản kiểm thử (Test Batch 1)

Mục tiêu: Đảm bảo script xử lý đa định dạng mà không lỗi.
- **File TXT**: Kiểm tra tốc độ và độ chính xác cơ bản.
- **File DOCX**: Kiểm tra khả năng đọc paragraph và bảng biểu đơn giản.
- **File PDF**: Kiểm tra khả năng xử lý khoảng trắng và ký tự lạ.
