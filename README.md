# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant built with FastAPI, Jinja2, HTML/CSS/JavaScript, and Google's Gemini API.

## Features

- Question & Answer
- Simplified topic explanations
- 5-question quiz generation
- Study-note summarization
- Personalized learning path
- Responsive web interface
- Health endpoint
- Render deployment configuration
- API endpoints matching the project document

## Project Structure

```text
EduGenie/
├── main.py
├── ai_service.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── render.yaml
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Local Setup - Windows PowerShell

Open PowerShell inside the project folder.

### 1. Create virtual environment

```powershell
py -3.10 -m venv venv
```

If `py -3.10` is not available, use:

```powershell
python -m venv venv
```

### 2. Install dependencies

You do not need to activate the environment.

```powershell
venv\Scripts\python.exe -m pip install --upgrade pip
venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Create `.env`

Copy `.env.example` to `.env` and add your Gemini API key.

Example:

```text
GEMINI_API_KEY=YOUR_REAL_KEY
GEMINI_MODEL=gemini-2.5-flash
```

Never upload `.env` to GitHub.

### 4. Start the app

```powershell
venv\Scripts\python.exe -m uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

Health check:

```text
http://127.0.0.1:8000/health
```

## API Endpoints

- `POST /qa`
- `POST /explain`
- `POST /quiz`
- `POST /summarize`
- `POST /learn/recommendations`
- `POST /api/generate`
- `GET /health`

## GitHub

```powershell
git init
git add .
git commit -m "Initial EduGenie project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Render

Create a Render Web Service from your GitHub repository.

Build command:

```text
pip install -r requirements.txt
```

Start command:

```text
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Environment variables:

```text
GEMINI_API_KEY = your real Gemini API key
GEMINI_MODEL = gemini-2.5-flash
```

You can also use the included `render.yaml`.

## Important

Do not commit or share your real Gemini API key. Use `.env` locally and Render Environment Variables for deployment.
