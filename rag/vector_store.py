import faiss
import numpy as np


def create_vector_store(embeddings):
    """
    Create a FAISS vector index.
    """

    if len(embeddings) == 0:
        return None

    embeddings = np.asarray(
        embeddings,
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(embeddings)

    return index


def search_vector_store(
    index,
    query_embedding,
    top_k=3
):
    """
    Search the FAISS vector store.
    """

    if index is None:
        return [], []

    query_embedding = np.asarray(
        [query_embedding],
        dtype="float32"
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    return distances[0], indices[0]