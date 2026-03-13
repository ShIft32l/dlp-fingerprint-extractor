import os
import argparse
import logging
from pathlib import Path
from tqdm import tqdm

from src.config import GEMINI_API_KEY
from src.parser import extract_document_text
from src.text_processor import clean_text, extract_long_phrases
from src.ai_evaluator import evaluate_phrases_batch
from src.generator import export_to_txt, export_to_csv

# Setup basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("dlp_extractor")

def run_pipeline(input_dir: str, output_path: str, doc_type: str, export_format: str):
    """Orchestrates the DLP Fingerprint extraction pipeline."""
    
    # 1. Parsing
    logger.info(f"Step 1: Parsing documents from {input_dir}...")
    all_raw_text = ""
    files_found = 0
    
    input_path = Path(input_dir)
    if not input_path.exists():
        logger.error(f"Input directory not found: {input_dir}")
        return

    # Find all supported files
    files = []
    for ext in [".txt", ".pdf", ".docx"]:
        files.extend(list(input_path.rglob(f"*{ext}")))
    
    if not files:
        logger.warning(f"No supported files found in {input_dir}")
        return

    for file_path in tqdm(files, desc="Parsing Docs"):
        text = extract_document_text(file_path)
        if text:
            all_raw_text += text + "\n"
            files_found += 1
    
    logger.info(f"Finished parsing {files_found} files.")

    # 2. Text Processing
    logger.info("Step 2: Cleaning text and extracting phrases...")
    cleaned_doc = clean_text(all_raw_text)
    phrases = extract_long_phrases(cleaned_doc)
    logger.info(f"Extracted {len(phrases)} candidate phrases.")

    if not phrases:
        logger.warning("No phrases extracted for evaluation.")
        return

    # 3. AI Evaluation
    logger.info(f"Step 3: Evaluating phrases with Gemini AI (Model: 1.5-flash)...")
    # Batch evaluation (AI Evaluator handles chunking internally if needed)
    selected_fingerprints = evaluate_phrases_batch(phrases)
    logger.info(f"AI kept {len(selected_fingerprints)} high-quality fingerprints.")

    # 4. Export
    logger.info(f"Step 4: Exporting results to {output_path} (Format: {export_format})...")
    if export_format.lower() == "txt":
        export_to_txt(selected_fingerprints, output_path)
    else:
        export_to_csv(selected_fingerprints, output_path, doc_type=doc_type)

    logger.info("✨ Pipeline completed successfully!")

def main():
    parser = argparse.ArgumentParser(description="DLP Fingerprint Extractor - Generate high-quality SITs using AI.")
    parser.add_argument("--input", "-i", type=str, required=True, help="Path to folder containing sample documents.")
    parser.add_argument("--output", "-o", type=str, default="output/fingerprints.txt", help="Path to save output file.")
    parser.add_argument("--type", "-t", type=str, default="Board Papers", help="Type of document for context (e.g., 'Board Papers').")
    parser.add_argument("--format", "-f", type=str, choices=["txt", "csv"], default="txt", help="Output format (txt or csv).")

    args = parser.parse_args()

    # Create output dir if needed (generator does this but good to have here too)
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)

    try:
        run_pipeline(args.input, args.output, args.type, args.format)
    except Exception as e:
        logger.error(f"❌ Pipeline failed: {e}")

if __name__ == "__main__":
    main()
