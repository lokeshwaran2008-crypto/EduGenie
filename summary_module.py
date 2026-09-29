from ai_service import generate_text

SYSTEM = """
You are EduGenie's summarization assistant.
Summarize the provided study material without changing its meaning.
Use a clear heading and concise bullet points.
Preserve important definitions, facts, formulas, and examples when present.
"""

def summarize_text(text: str) -> str:
    return generate_text(
        f"Summarize this study material:\n\n{text}",
        SYSTEM,
    )
