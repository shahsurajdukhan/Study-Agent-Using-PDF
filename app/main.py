import fitz

from llama_index.core import Document, VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


# Use a local embedding model
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)


# Path to your PDF
pdf_path = "data/operating_system.pdf"


# Extract text from PDF
documents = []

with fitz.open(pdf_path) as pdf:

    for page_number in range(len(pdf)):
        page = pdf[page_number]
        text = page.get_text()

        if text.strip():
            documents.append(
                Document(
                    text=text,
                    metadata={
                        "page": page_number + 1
                    }
                )
            )


print(f"Loaded {len(documents)} pages successfully.")


# Create LlamaIndex vector index
index = VectorStoreIndex.from_documents(documents)


# Create retriever
retriever = index.as_retriever(
    similarity_top_k=3
)


# Ask a question
question = input("\nAsk a question about your PDF: ")


# Retrieve relevant information
nodes = retriever.retrieve(question)


print("\nRelevant information:\n")

for i, node in enumerate(nodes, 1):

    print(f"--- Result {i} ---")

    print(node.text[:1000])

    print()