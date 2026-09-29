import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from explanation_module import explain_topic
from learning_path import recommend_learning_path
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

app = FastAPI(
    title="EduGenie - Google Gemini Powered Learning Assistant",
    version="1.0.0",
    description="AI-powered educational assistant using FastAPI and Google Gemini.",
)

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


class GenerateRequest(BaseModel):
    task: str = Field(..., min_length=1, max_length=40)
    prompt: str = Field(..., min_length=1, max_length=12000)


class TextRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=12000)


def run_task(task: str, prompt: str) -> str:
    task = task.strip().lower()

    if task == "qa":
        return answer_question(prompt)
    if task == "explain":
        return explain_topic(prompt)
    if task == "quiz":
        return generate_quiz(prompt)
    if task == "summarize":
        return summarize_text(prompt)
    if task in {"learning", "learning_path", "recommendations"}:
        return recommend_learning_path(prompt)

    raise HTTPException(
        status_code=400,
        detail="Invalid task. Use qa, explain, quiz, summarize, or learning.",
    )


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Compatible with current FastAPI/Starlette TemplateResponse API.
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"app_name": "EduGenie"},
    )


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "gemini_configured": bool(os.getenv("GEMINI_API_KEY")),
        "model": os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
    }


@app.post("/api/generate")
async def generate(request: GenerateRequest):
    try:
        return {"task": request.task, "result": run_task(request.task, request.prompt)}
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"AI request failed: {str(exc)}",
        ) from exc


# Endpoints matching the project document.
@app.post("/qa")
async def qa(request: TextRequest):
    return {"result": run_task("qa", request.prompt)}


@app.post("/explain")
async def explain(request: TextRequest):
    return {"result": run_task("explain", request.prompt)}


@app.post("/quiz")
async def quiz(request: TextRequest):
    return {"result": run_task("quiz", request.prompt)}


@app.post("/summarize")
async def summarize(request: TextRequest):
    return {"result": run_task("summarize", request.prompt)}


@app.post("/learn/recommendations")
async def learning_recommendations(request: TextRequest):
    return {"result": run_task("learning", request.prompt)}
