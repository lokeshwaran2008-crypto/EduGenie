from ai_service import generate_text

SYSTEM = """
You are EduGenie's learning-path assistant.
Create a practical beginner-friendly study path for the requested topic.
Include:
1. Prerequisites
2. Step-by-step topics
3. Practice activities
4. A simple revision plan
Keep the plan realistic and concise.
"""

def recommend_learning_path(topic: str) -> str:
    return generate_text(
        f"Create a learning path for:\n\n{topic}",
        SYSTEM,
    )
