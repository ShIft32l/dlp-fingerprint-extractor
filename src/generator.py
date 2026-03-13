import os
import csv
import logging
from typing import List, Union, Dict
from pathlib import Path
import pandas as pd

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

def export_to_csv(phrase_counts: Dict[str, int], selected_phrases: List[str], output_path: str, doc_type: str = "General"):
    """Exports selected phrases to a CSV file with Score (dummy placeholder), Count, and Category."""
    ensure_dir(output_path)
    try:
        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Phrase", "Count", "Score", "Type"])
            for phrase in selected_phrases:
                count = phrase_counts.get(phrase, 1)
                # Note: Currently score is implicit 1.0 because these are 'kept' phrases
                writer.writerow([phrase, count, "1.0", doc_type])
        logger.info(f"Successfully exported {len(selected_phrases)} phrases to {output_path}")
    except Exception as e:
        logger.error(f"Failed to export to CSV: {e}")
        raise

def export_to_excel(raw_data: List[Dict[str, str]], candidate_counts: Dict[str, int], selected_phrases: List[str], output_path: str):
    """
    Exports data to an Excel file with multiple sheets:
    - Sheet 1: Raw Extractions (Filename, Raw Text)
    - Sheet 2: Candidate Phrases (Processed phrases and Count)
    - Sheet 3: AI Recommended (Final phrases and Count)
    """
    ensure_dir(output_path)
    try:
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # 1. Raw Text Sheet
            if raw_data:
                df_raw = pd.DataFrame(raw_data)
                df_raw.to_excel(writer, sheet_name='Raw Extractions', index=False)
            
            # 2. Candidate Phrases Sheet
            if candidate_counts:
                df_candidates = pd.DataFrame([{
                    'Candidate Phrases': phrase,
                    'Count': count
                } for phrase, count in candidate_counts.items()])
                df_candidates = df_candidates.sort_values(by='Count', ascending=False)
                df_candidates.to_excel(writer, sheet_name='Candidate Phrases', index=False)
                
            # 3. AI Recommended Sheet
            if selected_phrases is not None:
                df_ai = pd.DataFrame([{
                    'AI Recommended': phrase,
                    'Count': candidate_counts.get(phrase, 1)
                } for phrase in selected_phrases])
                if not df_ai.empty:
                     df_ai = df_ai.sort_values(by='Count', ascending=False)
                df_ai.to_excel(writer, sheet_name='AI Recommended', index=False)
            else:
                # If skip-ai was used, write an empty sheet with a note
                df_ai = pd.DataFrame({'AI Recommended': ['(AI evaluation skipped via --skip-ai)'], 'Count': ['']})
                df_ai.to_excel(writer, sheet_name='AI Recommended', index=False)
                
        logger.info(f"Successfully exported detailed report to {output_path}")
    except Exception as e:
        logger.error(f"Failed to export to Excel: {e}")
        raise
