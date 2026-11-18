from rag.document_loader import load_document
from rag.text_splitter import split_text
from rag.embeddings import create_embeddings
from rag.vector_store import create_vector_store
from rag.retriever import retrieve_documents


# Load document
text = load_document(
    "documents/study_materials/test.txt"
)

print("Document loaded")
print("Characters:", len(text))


# Split document
chunks = split_text(text)

print("Chunks:", len(chunks))


# Create embeddings
embeddings = create_embeddings(chunks)

print("Embeddings created")


# Create vector store
vector_store = create_vector_store(
    embeddings
)

print("Vector store created")


# Ask question
question = "What is normalization?"

results = retrieve_documents(
    question,
    vector_store,
    chunks,
    top_k=3
)


print("\nRelevant information:\n")

for result in results:

    print(
        result["text"]
    )

    print(
        "Score:",
        result["score"]
    )

    print("-" * 50)