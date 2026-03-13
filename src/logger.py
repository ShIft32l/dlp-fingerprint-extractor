import logging
import sys
from .config import LOG_LEVEL

def get_logger(name: str) -> logging.Logger:
    """
    Creates and returns a configured logger instance.
    """
    logger = logging.getLogger(name)
    
    # Only configure if the logger has no handlers
    if not logger.handlers:
        level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
        logger.setLevel(level)

        # Create console handler
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(level)

        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Add formatter to console handler
        ch.setFormatter(formatter)

        # Add console handler to logger
        logger.addHandler(ch)

    return logger
