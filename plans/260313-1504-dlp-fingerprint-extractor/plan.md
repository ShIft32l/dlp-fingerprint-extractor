# Plan: DLP Fingerprint Extractor Tool
Created: 2026-03-13
Status: 🟡 In Progress

## Overview
DLP Fingerprint Extractor là một công cụ giúp tự động hóa việc trích xuất các cụm từ/câu văn mang tính đặc trưng cao (Fingerprint) từ các tài liệu mẫu (như Board Papers, Architectural Docs). Công cụ sử dụng Google Gemini AI để đánh giá và lọc các cụm từ này, tạo ra một danh sách Custom SIT (Sensitive Information Type) chất lượng cao nhằm nâng cao độ chính xác (giảm False Positive) cho hệ thống Microsoft Purview và Zscaler DLP.

## Tech Stack
-   **Ngôn ngữ chính:** Python 3.10+
-   **Xử lý tài liệu (Document Parsing):** 
    -   `PyPDF2` hoặc `pdfplumber` (cho file PDF)
    -   `python-docx` (cho file Word .docx)
-   **Xử lý văn bản (NLP/Text Processing):** `nltk` hoặc `spacy` (để tách câu, làm sạch dữ liệu cơ bản)
-   **AI Integration:** `google-generativeai` (Gemini API)
-   **Quản lý môi trường:** `python-dotenv` (quản lý API Key an toàn)

## Phases

| Phase | Name | Status | Progress |
|-------|------|--------|----------|
| 01 | Setup Environment & Utilities | ✅ Complete | 100% |
| 02 | Document Parser Module | ✅ Complete | 100% |
| 03 | Text Processing & Chunking | ✅ Complete | 100% |
| 04 | AI Evaluation Engine (Gemini) | ✅ Complete | 100% |
| 05 | Output Generator & CLI | ✅ Complete | 100% |
| 06 | Testing & Refinement | ✅ Complete | 100% |

## Quick Commands
- Start Phase 1: `/code phase-01`
- Check progress: `/next`
- Save context: `/save-brain`
