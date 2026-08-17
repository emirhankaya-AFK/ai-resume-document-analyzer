import re

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    filename: str = Field(min_length=1, max_length=255)
    text: str = Field(min_length=40, max_length=100_000)
    question: str | None = Field(default=None, max_length=500)


class AnalyzeResponse(BaseModel):
    filename: str
    summary: str
    skills: list[str]
    experience_years: int | None
    answer: str | None
    sources: list[str]


SKILLS = (
    "python",
    "fastapi",
    "flask",
    "django",
    "sql",
    "postgresql",
    "docker",
    "aws",
    "react",
    "typescript",
    "pytorch",
    "tensorflow",
    "nlp",
    "llm",
    "rag",
    "playwright",
)


def _skills(text: str) -> list[str]:
    lowered = text.lower()
    return [skill for skill in SKILLS if re.search(rf"\b{re.escape(skill)}\b", lowered)]


def _years(text: str) -> int | None:
    match = re.search(r"(\d+)\+?\s+years?", text.lower())
    return int(match.group(1)) if match else None


def _summary(text: str) -> str:
    sentences = re.split(r"(?<=[.!?])\s+", " ".join(text.split()))
    return " ".join(sentences[:2])[:400]


def _answer(text: str, question: str | None) -> str | None:
    if not question:
        return None
    terms = set(re.findall(r"[a-zA-Z]{3,}", question.lower()))
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    matches = []
    for line in lines:
        if terms.intersection(re.findall(r"[a-zA-Z]{3,}", line.lower())):
            matches.append(line)
    return " ".join(matches[:3]) if matches else "No grounded passage matched the question."


def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    return AnalyzeResponse(
        filename=request.filename,
        summary=_summary(request.text),
        skills=_skills(request.text),
        experience_years=_years(request.text),
        answer=_answer(request.text, request.question),
        sources=[request.filename],
    )


def create_app() -> FastAPI:
    app = FastAPI(title="AI Resume Document Analyzer", version="0.1.0")

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok", "service": "ai-resume-document-analyzer"}

    @app.post("/api/v1/analyze", response_model=AnalyzeResponse)
    async def analyze_document(request: AnalyzeRequest) -> AnalyzeResponse:
        if not request.filename.lower().endswith((".pdf", ".txt", ".docx")):
            raise HTTPException(status_code=415, detail="Use a PDF, TXT or DOCX filename")
        return analyze(request)

    return app


app = create_app()
