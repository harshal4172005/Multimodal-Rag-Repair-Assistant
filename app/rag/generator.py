"""Generates a grounded troubleshooting answer from retrieved manual chunks (text + diagrams)."""
from pathlib import Path

import google.generativeai as genai
from PIL import Image

from app.config import GEMINI_API_KEY, GENERATION_MODEL

genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = (
    "You are an appliance repair assistant. Answer the user's question using ONLY the "
    "provided manual excerpts and diagrams. Cite the page number for each fact you use. "
    "If the excerpts don't contain the answer, say so instead of guessing."
)

MAX_IMAGES = 4


def generate_answer(query: str, retrieved_chunks: list[dict]) -> str:
    context = "\n\n".join(
        f"[Page {c['page_number']}] {c['text']}" for c in retrieved_chunks
    )

    images = []
    for chunk in retrieved_chunks:
        for image_path in chunk["image_paths"]:
            if len(images) >= MAX_IMAGES:
                break
            if Path(image_path).exists():
                images.append(Image.open(image_path))

    model = genai.GenerativeModel(GENERATION_MODEL)
    prompt = f"{SYSTEM_PROMPT}\n\nManual excerpts:\n{context}\n\nQuestion: {query}"
    response = model.generate_content([prompt, *images])
    return response.text
