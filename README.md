# multimodal-rag-repair-assistant

Multimodal RAG assistant for home appliance & consumer electronics repair manuals.
Ingests PDF manuals (text + diagrams), embeds with Gemini, stores vectors in Qdrant,
and answers troubleshooting questions grounded in the retrieved manual pages.

## Status
Work in progress — ingestion pipeline (PDF text + image extraction, chunking) done.
Next: Gemini embeddings, Qdrant storage, retrieval, and the RAG answer generation + API.

## Stack
- FastAPI backend
- Google Gemini (embeddings + generation)
- Qdrant vector database
- PyMuPDF for PDF parsing

## Setup
1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and add your Gemini API key.
3. `docker compose up -d` to run Qdrant locally.
