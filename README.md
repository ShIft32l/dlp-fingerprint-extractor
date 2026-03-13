# DLP Fingerprint Extractor

DLP Fingerprint Extractor is a specialized tool designed to automate the extraction of high-quality "Fingerprints" (highly specific phrases) from corporate documents (Board Papers, Architecture Docs, etc.). These fingerprints are intended to be used as Custom Sensitive Information Types (SIT) in Microsoft Purview or Zscaler DLP systems.

## Key Features
- **Multi-format Support**: Parse text from `.pdf`, `.docx`, and `.txt` files.
- **Smart Text Processing**: Automatic cleaning of boilerplate text (headers, footers, signatures) and splitting into meaningful sentence candidates.
- **AI Evaluation**: Integration with Google Gemini (1.5 Flash) to score and filter candidate phrases based on organizational specificity.
- **Resilitent API Integration**: Built-in exponential backoff for handling Gemini API rate limits.

## Setup

1. **Install Dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configuration**:
   Copy `.env.example` to `.env` and add your [Gemini API Key](https://aistudio.google.com/apikey).
   ```bash
   cp .env.example .env
   # Edit .env with your key
   ```

## Usage (Development)

Currently, the project components can be tested individually:
- Test Parser: `python src/tests_dummy.py`
- Test Text Processor: `python src/test_text_processor.py`
- Test AI Evaluator: `python src/test_ai_evaluator.py`

## Next Phases
- Phase 05: Output Generator & CLI Interface
- Phase 06: Integration Testing & Bulk Processing
