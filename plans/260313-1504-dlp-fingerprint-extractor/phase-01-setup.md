# Phase 01: Setup Environment & Utilities
Status: ⬜ Pending

## Objective
Khởi tạo cấu trúc dự án cơ bản và thiết lập môi trường để xử lý các thư viện NLP cơ bản, cũng như chuẩn bị các utility (tiện ích/hàm chung) để log lỗi và quản lý config.

## Requirements
### Functional
- [ ] Script có thể chạy được từ terminal (CLI tool).
- [ ] Có file `.env` chứa API keys và cấu hình.
- [ ] Có hệ thống logging đơn giản ghi vào console hoặc file.

## Implementation Steps
1. [x] Cài đặt môi trường ảo (`python -m venv venv`) (Hướng dẫn user chạy thủ công nếu cần).
2. [x] Tạo file `requirements.txt` chuyên trích xuất text và NLP (PyPDF2, python-docx, python-dotenv, google-generativeai, nltk, spacy).
3. [x] Tạo cấu trúc thư mục module `src/`.
4. [x] Tạo file `.env.example`.
5. [x] Cấu hình logging cơ bản (file `src/logger.py`).
6. [x] Tạo file Config/Loader đọc `.env` (`src/config.py`).

## Files to Create/Modify
- `requirements.txt` - Dependencies library cho project.
- `.env.example` - Template các biến cấu hình (VD: `GEMINI_API_KEY`).
- `src/__init__.py`
- `src/logger.py` - Hệ thống log ra console (INFO/ERROR).
- `src/config.py` - Chịu trách nhiệm load môi trường từ `dotenv`.

## Test Criteria
- [x] Chạy `python src/config.py` không văng lỗi khi thiếu `.env`.
- [x] Log message test hiển thị đúng định dạng.

---
Next Phase: phase-02-parser.md
