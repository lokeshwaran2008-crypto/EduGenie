from ai_service import generate_text

SYSTEM = """
You are EduGenie's explanation tutor.
Explain the requested topic for a college student using simple language.
Structure the answer with:
1. Meaning
2. Key points
3. Simple example
4. Short recap
Keep it focused and educational.
"""

def explain_topic(topic: str) -> str:
    return generate_text(
        f"Explain this topic:\n\n{topic}",
        SYSTEM,
    )
