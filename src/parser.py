import logging
from pathlib import Path
from typing import Optional, Union
import PyPDF2
from docx import Document

logger = logging.getLogger(__name__)

def read_txt(path: Path) -> Optional[str]:
    """Reads raw text from a .txt file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error reading TXT file {path}: {e}")
        return None

def read_docx(path: Path) -> Optional[str]:
    """Reads text from a MS Word .docx file."""
    try:
        doc = Document(str(path))
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return "\n".join(full_text)
    except Exception as e:
        logger.error(f"Error reading DOCX file {path}: {e}")
        return None

def read_pdf(path: Path) -> Optional[str]:
    """Reads text from a PDF file."""
    try:
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text_blocks = []
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text_blocks.append(extracted)
            return "\n".join(text_blocks)
    except Exception as e:
        logger.error(f"Error reading PDF file {path}: {e}")
        return None

def extract_document_text(path: Union[str, Path]) -> Optional[str]:
    """Factory function to extract text based on file suffix."""
    file_path = Path(path)
    
    if not file_path.exists():
        logger.warning(f"File not found: {file_path}")
        return None
    
    if not file_path.is_file():
        logger.warning(f"Path is not a regular file: {file_path}")
        return None

    suffix = file_path.suffix.lower()
    
    if suffix == ".txt":
        return read_txt(file_path)
    elif suffix == ".docx":
        return read_docx(file_path)
    elif suffix == ".pdf":
        return read_pdf(file_path)
    else:
        logger.warning(f"Unsupported file format '{suffix}' for file: {file_path}")
        return None
