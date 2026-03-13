"""
AI Evaluation Engine — Google GenAI (google-genai) SDK
- Sends candidate phrases to Google Gemini for DLP fingerprint scoring
- Returns only the highly-specific phrases suitable for Custom SIT / DLP Dictionary
"""

import json
import time
import logging
import re
from typing import List, Optional

from google import genai
from google.genai import types

from .config import GEMINI_API_KEY

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Gemini configuration
# ---------------------------------------------------------------------------
_MODEL_NAME = "gemini-flash-latest"
_MAX_RETRIES = 5
_RETRY_BASE_DELAY = 5  # seconds, doubles each retry (5, 10, 20, 40, 80)
_BATCH_SIZE = 30  # max phrases per API call
_INTER_BATCH_DELAY = 2.0  # seconds between batches (rate limiter)


def _get_client() -> genai.Client:
    """Create and return a GenAI client."""
    return genai.Client(api_key=GEMINI_API_KEY)


# ---------------------------------------------------------------------------
# Prompt Engineering
# ---------------------------------------------------------------------------
_SYSTEM_INSTRUCTION = """\
You are an expert Data Loss Prevention (DLP) analyst specializing in document fingerprinting.

Your task: Given a numbered list of phrases extracted from corporate documents, identify ONLY the phrases that are **highly specific to a particular organization or document type**.

### Selection criteria — KEEP phrases that:
- Contain proper nouns, project names, internal code-names, product names
- Reference specific financial figures, dates tied to decisions, or named strategies
- Describe proprietary processes, architectures, or internal policies
- Would almost certainly NOT appear in a generic, publicly-available document

### Removal criteria — DISCARD phrases that:
- Are generic greetings, sign-offs, or pleasantries ("Dear colleagues", "Best regards")
- Are common business language that could appear in ANY company ("revenue growth", "next steps")
- Contain only dates, page numbers, or formatting artifacts
- Are too short or vague to be a reliable fingerprint

### Output format
Return ONLY a JSON array of the selected phrases (strings). Nothing else.
Example: ["phrase one kept", "phrase two kept"]
If no phrases qualify, return an empty array: []
"""


def _build_user_prompt(phrases: List[str]) -> str:
    """Build the user-facing prompt with the numbered phrase list."""
    numbered = "\n".join(f"{i+1}. {p}" for i, p in enumerate(phrases))
    return (
        f"Below are {len(phrases)} candidate phrases extracted from corporate documents.\n"
        f"Apply the selection criteria and return ONLY the JSON array of kept phrases.\n\n"
        f"{numbered}"
    )


# ---------------------------------------------------------------------------
# Core evaluation
# ---------------------------------------------------------------------------
def _call_gemini(client: genai.Client, phrases: List[str]) -> List[str]:
    """
    Send a single batch of phrases to Gemini and parse the JSON array response.
    Includes retry logic for transient / quota errors.
    """
    user_prompt = _build_user_prompt(phrases)

    for attempt in range(1, _MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model=_MODEL_NAME,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=_SYSTEM_INSTRUCTION,
                    temperature=0.1,
                    max_output_tokens=4096,
                ),
            )

            raw_text = response.text.strip()

            # Try to extract JSON array from the response
            parsed = _parse_json_array(raw_text)
            if parsed is not None:
                return parsed

            logger.warning(
                "Gemini response was not a valid JSON array (attempt %d/%d). Raw: %s",
                attempt, _MAX_RETRIES, raw_text[:300],
            )

        except Exception as e:
            error_str = str(e)
            # Rate limit / quota error — back off
            if "429" in error_str or "quota" in error_str.lower() or "resource" in error_str.lower():
                delay = _RETRY_BASE_DELAY * (2 ** (attempt - 1))
                logger.warning("Rate limited (429). Sleeping %ds before retry %d/%d", delay, attempt, _MAX_RETRIES)
                time.sleep(delay)
            else:
                logger.error("Gemini API error (attempt %d/%d): %s", attempt, _MAX_RETRIES, e)
                if attempt < _MAX_RETRIES:
                    time.sleep(_RETRY_BASE_DELAY)

    logger.error("All %d Gemini attempts failed for batch of %d phrases.", _MAX_RETRIES, len(phrases))
    return []


def _parse_json_array(text: str) -> Optional[List[str]]:
    """
    Attempt to parse a JSON array of strings from Gemini's response.
    Handles cases where the response is wrapped in markdown code fences.
    """
    # Strip markdown code fences if present
    cleaned = re.sub(r"^```(?:json)?\s*", "", text, flags=re.MULTILINE)
    cleaned = re.sub(r"```\s*$", "", cleaned, flags=re.MULTILINE)
    cleaned = cleaned.strip()

    try:
        result = json.loads(cleaned)
        if isinstance(result, list) and all(isinstance(item, str) for item in result):
            return result
    except json.JSONDecodeError:
        pass

    # Fallback: try to find a JSON array substring
    match = re.search(r"\[.*\]", cleaned, re.DOTALL)
    if match:
        try:
            result = json.loads(match.group())
            if isinstance(result, list):
                return [str(item) for item in result]
        except json.JSONDecodeError:
            pass

    return None


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------
def evaluate_phrases_batch(phrases: List[str]) -> List[str]:
    """
    Evaluate a list of candidate phrases using Gemini AI.

    Splits into batches of _BATCH_SIZE, sends each batch to the API,
    and returns a deduplicated list of phrases that Gemini considers
    highly specific / suitable for DLP fingerprinting.

    Args:
        phrases: List of candidate phrase strings.

    Returns:
        List of filtered phrases deemed specific enough for DLP.
    """
    if not phrases:
        return []

    client = _get_client()

    all_kept: List[str] = []
    total_batches = (len(phrases) + _BATCH_SIZE - 1) // _BATCH_SIZE

    for batch_idx in range(total_batches):
        start = batch_idx * _BATCH_SIZE
        end = start + _BATCH_SIZE
        batch = phrases[start:end]

        logger.info(
            "Evaluating batch %d/%d (%d phrases)...", batch_idx + 1, total_batches, len(batch)
        )

        kept = _call_gemini(client, batch)
        all_kept.extend(kept)

        # Rate limiter: sleep between batches (except after the last one)
        if batch_idx < total_batches - 1:
            logger.debug("Rate limiter: sleeping %.1fs before next batch", _INTER_BATCH_DELAY)
            time.sleep(_INTER_BATCH_DELAY)

    # Deduplicate while preserving order
    seen = set()
    deduplicated: List[str] = []
    for phrase in all_kept:
        key = phrase.lower()
        if key not in seen:
            seen.add(key)
            deduplicated.append(phrase)

    logger.info(
        "AI evaluation complete: %d input phrases → %d fingerprints kept.",
        len(phrases), len(deduplicated),
    )
    return deduplicated
