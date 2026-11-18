from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_embeddings(text_chunks):
    """
    Convert text chunks into numerical vectors.
    """

    if not text_chunks:
        return []

    embeddings = model.encode(
        text_chunks,
        convert_to_numpy=True
    )

    return embeddings