import fitz

from typing import TypedDict

from llama_index.core import Document , VectorStoreIndex , Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from langgraph.graph import StateGraph, START, END

# LlamaIndex Setup

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

PDF_PATH = "data/operating_system.pdf"


documents = [] 

with fitz.open(PDF_PATH) as pdf:
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


print (f"Loaded {len(documents)} pages.")


# Create Vector index
index = VectorStoreIndex.from_documents(documents)

# Create retriever
retriever = index.as_retriever(
    similarity_top_k=3
)


# 2. LangGraph State

class AgentState(TypedDict):
    question: str
    needs_context: bool
    context: str
    answer: str



# 3.  Analyze Question 
def analyze_question(state: AgentState):
    question = state["question"].lower()

    keywords = [
        "according to the document"
        "in the document"
        "from the document"
        "what does the document"
        "what is"
        "explain"
        "define"
    ]

    needs_context = any (
        keyword in question
        for keyword in keywords
    )

    return {
        "needs_context": needs_context
    }


# 4. Retreive Context using LlamaIndex

def retrieve_context(state: AgentState):

    question = state["question"]

    print("\nSearching LlamaIndex...")

    nodes = retriever.retrieve(question)

    print(f"Retrieved nodes: {len(nodes)}")

    context_parts = []

    for i, node in enumerate(nodes, 1):

        text = node.get_content()

        page = node.metadata.get("page", "unknown")

        print(f"\n--- Node {i} | Page {page} ---")
        print(text[:500])

        context_parts.append(
            f"[Page {page}]\n{text}"
        )

    context = "\n\n".join(context_parts)

    return {
        "context": context
    }


# 5. Temporary General Response 

def general_response(state: AgentState):

    return {
        "answer": "This question does not require document retrieval." 
    }


# 6. Route Question 
def route_question(state: AgentState):

    if state["needs_context"]:
        return "retrieve"

    return "general"


# 7. Build LangGraph

builder = StateGraph(AgentState)

builder.add_node(
    "analyze",
    analyze_question
)

builder.add_node(
    "retrieve",
    retrieve_context
)

builder.add_node(
    "general",
    general_response
)

builder.add_edge(

    START,
    "analyze"
)

builder.add_edge(
    "analyze",
    "retrieve"
)

builder.add_edge(
    "retrieve",
    END
)

graph = builder.compile()


# 8. Run the Agent

if __name__ == "__main__":

    question = input(
        "\n Ask a question about your PDF: "
    )

    result = graph.invoke(
        {
            "question" : question,
            "needs_context" : False,
            "context" : "",
            "answer": ""
        }
    )

    print("\n=============================")
    print("RETRIEVED CONTEXT")
    print("===============================\n")

    print(
        result.get(
            "context",
            result.get("answer","")
        )
    )