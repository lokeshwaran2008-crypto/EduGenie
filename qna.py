from ai_service import generate_text

SYSTEM = """
You are EduGenie, a friendly educational assistant.
Answer student questions clearly and accurately.
Use simple language, short sections, and examples when useful.
Do not invent facts. If the question is ambiguous, state the assumption.
"""

def answer_question(question: str) -> str:
    return generate_text(
        f"Answer this student's question:\n\n{question}",
        SYSTEM,
    )
