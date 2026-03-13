import os
import csv
import logging
from typing import List, Union
from pathlib import Path

logger = logging.getLogger(__name__)

def ensure_dir(path: Union[str, Path]):
    """Ensures that the directory for the given path exists."""
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
        logger.info(f"Created directory: {directory}")

def export_to_txt(phrases: List[str], output_path: str):
    """Exports phrases to a plain text file, one per line."""
    ensure_dir(output_path)
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            for phrase in phrases:
                f.write(f"{phrase}\n")
        logger.info(f"Successfully exported {len(phrases)} phrases to {output_path}")
    except Exception as e:
        logger.error(f"Failed to export to TXT: {e}")
        raise

def export_to_csv(phrases: List[str], output_path: str, doc_type: str = "General"):
    """Exports phrases to a CSV file with Score and Category (dummy placeholder)."""
    ensure_dir(output_path)
    try:
        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Phrase", "Score", "Type"])
            for phrase in phrases:
                # Note: Currently score is implicit 1.0 because these are 'kept' phrases
                writer.writerow([phrase, "1.0", doc_type])
        logger.info(f"Successfully exported {len(phrases)} phrases to {output_path}")
    except Exception as e:
        logger.error(f"Failed to export to CSV: {e}")
        raise
