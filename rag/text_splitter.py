def split_text(
    text,
    chunk_size=500,
    chunk_overlap=50
):
    """
    Split document text into overlapping chunks.
    """

    if not text:
        return []

    text = text.replace("\r", " ").replace("\n", " ")

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(
            words[start:end]
        )

        if chunk.strip():
            chunks.append(chunk.strip())

        start = end - chunk_overlap

        if start < 0:
            start = 0

    return chunks