"""CLI: ask a troubleshooting question against ingested manuals. Usage: python -m app.ask "<question>" """
import sys

from app.rag.generator import generate_answer
from app.rag.retriever import retrieve_chunks


def ask(query: str) -> str:
    chunks = retrieve_chunks(query)
    return generate_answer(query, chunks)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python -m app.ask "<question>"')
        sys.exit(1)
    print(ask(sys.argv[1]))
