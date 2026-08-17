# AI Resume / Document Analyzer

[English](README.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md)

FastAPI-MVP für CV- und Dokumentanalyse. Der Dienst liefert Zusammenfassung, erkannte Skills, Berufserfahrung, eine textbasierte Antwort und die Quelldatei.

![Demo](docs/demo.svg)

## Funktionen
- PDF-, TXT- und DOCX-kompatibler Analysevertrag
- Skill- und Erfahrungsjahre-Extraktion
- Grounded Antwort mit Quellenname
- Docker, Tests und CI

## Start

    pip install -e ".[dev]"
    uvicorn app.main:app --reload
    pytest -q

Die aktuelle Version verarbeitet bereits extrahierten Text. PDF-Parser, OCR, Embeddings/RAG und ein LLM-Provider sind klare nächste Adapter.

