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

## Usage

The tool is executed via the `main.py` entry point. It automates the entire pipeline: Parsing → Processing → AI Evaluation → Export.

```bash
python3 main.py --input path/to/docs --output output/fingerprints.txt --format txt --type "Board Papers"
```

### Options:
- `--input`, `-i`: (Required) Path to the folder containing your sample `.pdf`, `.docx`, or `.txt` files.
- `--output`, `-o`: Path to the output file (Default: `output/fingerprints.txt`).
- `--format`, `-f`: Output format (`txt` or `csv`). TXT is recommended for direct DLP dictionary import.
- `--type`, `-t`: Contextual hint for AI (e.g., "Board Papers", "Financial Reports"). Helps AI understand what is "generic" vs "specific".

## Directory Structure

- `main.py`: Main execution orchestrator.
- `src/`:
  - `parser.py`: Document text extraction.
  - `text_processor.py`: Cleaning and phrase filtering.
  - `ai_evaluator.py`: Gemini AI scoring logic.
  - `generator.py`: Output file creation.
  - `config.py`: Environment and API settings.
- `docs/`:
  - `BRIEF.md`: Project overview and goals.
  - `REQUIREMENTS_TESTING.md`: AI quality criteria and prompt strategy.

## Verification

You can verify the setup by running the pipeline on the provided batch samples:
```bash
python3 main.py --input ./samples/test_batch_1 --output output/test_results.txt
```
