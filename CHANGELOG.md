# Changelog

All notable changes to this project will be documented in this file.

## [2026-03-13]
### Added
- **Project Structure**: Initial setup with `src`, `docs`, `plans`, and `samples` folders.
- **Environment Logic**: `.env` configuration for Gemini API keys and logging.
- **Document Parser**: `src/parser.py` supports text extraction from `.txt`, `.docx`, `.pdf`, `.xlsx`, and `.pptx`.
- **Text Processor**: `src/text_processor.py` for cleaning text, splitting into sentences (NLTK), filtering long phrases for DLP, and tracking duplicate text frequencies.
- **AI Evaluation**: `src/ai_evaluator.py` using Gemini 1.5 Flash (google-genai) to score and filter specific DLP fingerprints.
- **Generator**: Exporting logic now supports outputting to `.xlsx` files with multiple sheets and detailed reporting.
- **CLI Pipelines**: Added `--skip-ai` and `--format excel` flags.
- **Testing**: Test scripts for each component (`src/test_*.py`).

### Changed
- Migrated from deprecated `google.generativeai` to `google-genai` SDK.
- Switched default model to `gemini-1.5-flash` for better rate-limit stability.

### Fixed
- Fixed 429 Rate Limit issues by implementing exponential backoff.
- Fixed Python 3.9 type hinting compatibility.
