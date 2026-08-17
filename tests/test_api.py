from fastapi.testclient import TestClient

from app.main import AnalyzeRequest, analyze, create_app


def test_analyzer_extracts_skills_and_grounded_answer() -> None:
    result = analyze(
        AnalyzeRequest(
            filename="resume.pdf",
            text=(
                "Python and FastAPI engineer with 5 years experience. "
                "Built RAG services with PostgreSQL."
            ),
            question="Tell me about FastAPI",
        )
    )
    assert "python" in result.skills
    assert result.experience_years == 5
    assert "FastAPI" in (result.answer or "")
    assert result.sources == ["resume.pdf"]


def test_filename_is_validated() -> None:
    with TestClient(create_app()) as client:
        response = client.post("/api/v1/analyze", json={"filename": "image.png", "text": "a" * 50})
    assert response.status_code == 415
