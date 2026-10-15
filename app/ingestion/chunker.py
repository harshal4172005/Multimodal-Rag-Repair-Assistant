"""Splits page text into overlapping chunks for embedding."""


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 150) -> list[str]:
    if not text:
        return []
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end].strip())
        start = end - overlap
    return [c for c in chunks if c]


def demo():
    sample = "A" * 2000
    chunks = chunk_text(sample, chunk_size=800, overlap=150)
    assert len(chunks) == 4
    assert all(len(c) <= 800 for c in chunks)
    assert chunk_text("") == []
    print("chunker self-check passed:", len(chunks), "chunks")


if __name__ == "__main__":
    demo()
