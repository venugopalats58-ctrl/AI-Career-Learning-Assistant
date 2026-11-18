from .embeddings import model
from .vector_store import search_vector_store


def retrieve_documents(
    query,
    vector_store,
    text_chunks,
    top_k=3
):
    """
    Retrieve the most relevant document chunks
    for a user question.
    """

    if not query or vector_store is None:
        return []

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )[0]

    distances, indices = search_vector_store(
        vector_store,
        query_embedding,
        top_k
    )

    results = []

    for distance, index in zip(
        distances,
        indices
    ):

        if index < 0:
            continue

        if index >= len(text_chunks):
            continue

        results.append({
            "text": text_chunks[index],
            "score": float(distance)
        })

    return results