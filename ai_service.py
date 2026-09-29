import os
from functools import lru_cache

from google import genai
from google.genai import types


def _get_api_key() -> str:
    key = os.getenv("GEMINI_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Add it to your .env file locally "
            "or to Render Environment Variables."
        )
    return key


def _get_model() -> str:
    return os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()


@lru_cache(maxsize=1)
def get_client() -> genai.Client:
    return genai.Client(api_key=_get_api_key())


def generate_text(prompt: str, system_instruction: str) -> str:
    response = get_client().models.generate_content(
        model=_get_model(),
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.4,
            max_output_tokens=1200,
        ),
    )
    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty response.")
    return text.strip()
