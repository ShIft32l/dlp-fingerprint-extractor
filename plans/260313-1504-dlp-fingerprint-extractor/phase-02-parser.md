# Phase 02: Document Parser Module
Status: ⬜ Pending

## Objective
Xây dựng một module chung cho việc đọc và trích xuất text thô từ các định dạng file phổ biến: .txt, .pdf, .docx.

## Requirements
### Functional
- [ ] Hàm `extract_text_from_file(filepath)` trả về chuỗi Unicode thông qua abstract/interface hỗ trợ đa định dạng.
- [ ] Bỏ qua các file không được hỗ trợ và log lại cảnh báo (Warning).
- [ ] Quản lý đường dẫn filepath bằng thư viện `pathlib`.

## Implementation Steps
1. [ ] Tạo file `src/parser.py`.
2. [ ] Viết hàm đọc file mộc `read_txt(path)`.
3. [ ] Viết hàm đọc file Word bằng module `python-docx` (`read_docx(path)`).
4. [ ] Viết hàm đọc PDF bằng module `PyPDF2` (hoặc nâng cao là `pdfplumber`) (`read_pdf(path)`).
5. [ ] Viết hàm Factory phân phối Logic dựa trên phần mở rộng (`.suffix`) của file `extract_document_text(path)`.

## Files to Create/Modify
- `src/parser.py` - Chịu trách nhiệm Input Text Parsing.

## Test Criteria
- [ ] Parse một file `dummy.txt` chuẩn xác.
- [ ] Parse một file `dummy.docx` chuẩn xác (có chữ/số đặc biệt).
- [ ] Parse một file `dummy.pdf` chuẩn xác (lấy được các block text).

---
Next Phase: phase-03-processing.md
