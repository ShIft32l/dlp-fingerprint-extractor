# 💡 BRIEF: DLP Document Fingerprint Extractor (SIT Generator)

**Ngày tạo:** 2026-03-13
**Khách hàng mục tiêu:** Team Security - Triển khai cho giải pháp MS Purview & Zscaler DLP

---

## 1. VẤN ĐỀ CẦN GIẢI QUYẾT
Tính năng Document Fingerprinting (IDM) mặc định của Microsoft Purview và Zscaler không hoạt động hiệu quả/chính xác với các tài liệu đặc thù của doanh nghiệp (VD: Board Papers, Architecture Documents). Việc sử dụng keywords đơn lẻ dễ dẫn đến tỷ lệ False Positive (cảnh báo nhầm) cao.

## 2. GIẢI PHÁP ĐỀ XUẤT
Xây dựng một Tool/Script tự động đọc các tài liệu mẫu (sample documents), trích xuất các cụm từ dài đặc trưng (> 5 tokens), và sử dụng AI (như Gemini) để đánh giá/lọc lại danh sách này. Output sẽ là một file chứa các cụm từ "chất lượng cao" dùng để tạo Custom SIT (Sensitive Information Type) / DLP Dictionary nạp ngược lại vào Purview/Zscaler.

## 3. ĐỐI TƯỢNG SỬ DỤNG
- **Primary:** Admin / Security Engineer quản trị hệ thống DLP.
- **Môi trường:** Dùng nội bộ, chạy dạng Script/CLI Tool.

## 4. TÍNH NĂNG CHÍNH

### 🚀 MVP (Dự kiến hoàn thành trước):
- [ ] **Document Parser:** Hỗ trợ đọc nhiều định dạng file mẫu khác nhau (PDF, Word, TXT) từ một thư mục chỉ định.
- [ ] **Text Extractor & Pre-processing:** Dọn dẹp văn bản (loại bỏ khoảng trắng thừa, ký tự đặc biệt) và trích xuất các câu/cụm từ dài (N-grams > 5 tokens).
- [ ] **AI Evaluator (Gemini Integration):** Gửi các cụm từ đã trích xuất qua Gemini API kèm theo Prompt đặc chế để AI chấm điểm và lọc ra những cụm từ "đặc thù nhất" của loại tài liệu đó, loại bỏ câu từ chung chung.
- [ ] **Output Generator:** Xuất danh sách các cụm từ đạt chuẩn ra định dạng file dễ copy/paste (TXT, CSV) để import vào MS Purview/Zscaler.

### 🎁 Phase 2 (Nâng cấp sau):
- [ ] **Local AI Support:** Hỗ trợ gọi các model AI local (như Ollama) để xử lý các tài liệu cực kỳ nhạy cảm mà không được phép đẩy lên API public.
- [ ] **GUI/Dashboard Interface:** Giao diện Web đơn giản thay vì chạy lệnh CLI.

## 5. ƯỚC TÍNH SƠ BỘ
- **Độ phức tạp:** Trung bình - Cần xử lý text (thư viện như `pdfplumber`, `python-docx`) và tối ưu Prompt khi gọi Gemini API.
- **Rủi ro:** 
  - Token Limit khi gọi Google Gemini API nếu tài liệu quá dài (cần giải pháp chia nhỏ text - chunking).
  - Tỷ lệ nhiễu văn bản (header, footer, số trang) khi extract từ PDF.

## 6. KHÍA CẠNH KỸ THUẬT (Đề xuất)
- **Ngôn ngữ/Môi trường:** Python (rất mạnh về xử lý NLP và tương tác API).

## 7. BƯỚC TIẾP THEO
→ Chạy `/plan` để lên thiết kế chi tiết (Luồng xử lý, cấu trúc Prompt, thư viện sử dụng).
