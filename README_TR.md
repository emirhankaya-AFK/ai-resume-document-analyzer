# AI Resume / Document Analyzer

[English](README.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md)

CV ve PDF metni için FastAPI doküman zekâsı MVP'si. Özet, tespit edilen beceriler, deneyim yılı, metne dayalı cevap ve kaynak dosya adını döndürür.

![Demo](docs/demo.svg)

## Teknolojiler
Python, FastAPI, Pydantic, deterministik çıkarım, Docker, pytest ve GitHub Actions. Dikey akış metin alır; üretimde PDF/DOCX parser, OCR, embedding/RAG, PostgreSQL ve LLM sağlayıcısı eklenebilir.

## API ve çalıştırma
POST /api/v1/analyze filename, text ve isteğe bağlı question alır. Yalnızca PDF, TXT ve DOCX dosya adları kabul edilir.

    pip install -e ".[dev]"
    uvicorn app.main:app --reload
    pytest -q

Docker: docker compose up --build. API dokümanı: /docs.

Cevap yalnızca gönderilen metne dayalıdır ve işe alım kararı değildir.
