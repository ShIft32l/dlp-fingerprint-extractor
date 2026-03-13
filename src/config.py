import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define configuration variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Verify critical configurations
if not GEMINI_API_KEY or GEMINI_API_KEY == "your_gemini_api_key_here":
    import warnings
    warnings.warn("GEMINI_API_KEY is not set or using the default template value. API calls will fail.")
