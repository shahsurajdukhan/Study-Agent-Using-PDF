#  Study Agent Using PDF

A lightweight **AI-powered PDF question-answering agent** built with **LlamaIndex, LangChain, and LangGraph**.

The project allows users to provide a PDF document and ask questions about its content. The system extracts the document text, creates a searchable vector index, retrieves the most relevant information, and will use an LLM-based workflow to generate contextual answers.

> 🚧 **Project Status:** In Development
> The current version implements PDF text extraction and LlamaIndex-based retrieval. LangGraph routing and LangChain LLM generation are the next development stages.

---

## ✨ Features

* 📄 Read and process PDF documents
* 🔎 Extract clean text from PDF pages
* 🧠 Generate local embeddings using Hugging Face
* 📚 Build a vector index using LlamaIndex
* 🔍 Retrieve the most relevant document sections
* 🧩 Conditional workflow using LangGraph
* 🤖 LLM-based answer generation using LangChain
* 🔐 Keep API keys outside the repository using `.env`
* 🐍 Built entirely with Python

---

## 🏗️ Architecture

The planned architecture combines three popular AI frameworks, with each framework having a specific responsibility:

```text
                         User Question
                              │
                              ▼
                    ┌──────────────────┐
                    │    LangGraph     │
                    │ Workflow / Router│
                    └─────────┬────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │    LlamaIndex    │
                    │ Document Retrieval│
                    └─────────┬────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │    LangChain     │
                    │   LLM / Prompt   │
                    └─────────┬────────┘
                              │
                              ▼
                       Final Answer
```

### Framework Responsibilities

| Technology       | Responsibility                                   |
| ---------------- | ------------------------------------------------ |
| **LlamaIndex**   | PDF indexing, embeddings, and document retrieval |
| **LangGraph**    | Workflow orchestration and conditional routing   |
| **LangChain**    | LLM integration and prompt/response generation   |
| **PyMuPDF**      | PDF text extraction                              |
| **Hugging Face** | Local embedding model                            |

---

## 🔄 Current Data Flow

The currently implemented retrieval pipeline works like this:

```text
PDF
 │
 ▼
PyMuPDF
 │
 ▼
Extract text from each page
 │
 ▼
LlamaIndex Document
 │
 ▼
Hugging Face Embeddings
 │
 ▼
VectorStoreIndex
 │
 ▼
Retriever
 │
 ▼
Relevant document chunks
```

The final agent will extend this into:

```text
Question
   │
   ▼
LangGraph
   │
   ├── Document question
   │       │
   │       ▼
   │   LlamaIndex Retriever
   │       │
   │       ▼
   │   Relevant Context
   │
   └── General question
           │
           ▼
       LLM
           │
           ▼
        Answer
```

---

# 🛠️ Tech Stack

### Programming Language

* Python 3.10+

### AI / LLM Frameworks

* [LangChain](https://www.langchain.com/)
* [LangGraph](https://www.langchain.com/langgraph)
* [LlamaIndex](https://www.llamaindex.ai/)

### Document Processing

* PyMuPDF

### Embeddings

* Hugging Face
* `BAAI/bge-small-en-v1.5`

### Environment Management

* Python Virtual Environment
* `python-dotenv`

### Version Control

* Git
* GitHub

---

# 📁 Project Structure

```text
Study-Agent-Using-PDF/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── graph.py
│
├── data/
│   └── your_pdf.pdf
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
```

### File Description

| File / Folder      | Purpose                                 |
| ------------------ | --------------------------------------- |
| `app/main.py`      | PDF extraction, indexing, and retrieval |
| `app/graph.py`     | LangGraph workflow                      |
| `app/__init__.py`  | Python package initialization           |
| `data/`            | PDF documents used by the application   |
| `.env`             | Environment variables and API keys      |
| `.gitignore`       | Files that should not be committed      |
| `requirements.txt` | Python dependencies                     |
| `README.md`        | Project documentation                   |

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/shahsurajdukhan/Study-Agent-Using-PDF.git
```

Move into the project directory:

```bash
cd Study-Agent-Using-PDF
```

---

## 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

You should see:

```text
(venv)
```

at the beginning of your terminal.

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

If PyMuPDF is not already installed:

```bash
pip install pymupdf
```

---

## 4. Add your PDF

Place a PDF inside:

```text
data/
```

For example:

```text
data/
└── operating_system_notes.pdf
```

Then update the PDF path in `app/main.py`:

```python
pdf_path = "data/operating_system_notes.pdf"
```

---

# ▶️ Running the Project

Run the application from the project root:

```bash
python app/main.py
```

The application will process the PDF and create a searchable LlamaIndex vector index.

You will then be prompted:

```text
Ask a question about your PDF:
```

Example:

```text
What is the main objective of an operating system?
```

The system retrieves the most relevant sections from the document.

---

# 🧠 How Retrieval Works

The application uses a local embedding model:

```text
BAAI/bge-small-en-v1.5
```

The process is:

```text
PDF
 ↓
Text Extraction
 ↓
Documents
 ↓
Embeddings
 ↓
Vector Store
 ↓
Similarity Search
 ↓
Top Relevant Results
```

For example, if the PDF contains information about operating systems and the user asks:

```text
What is the primary objective of an operating system?
```

the retriever searches the indexed document and returns the most semantically relevant sections.

---

# 🧩 LangGraph Workflow

LangGraph is used to represent the agent as a workflow rather than a single linear function.

The planned workflow is:

```text
START
  │
  ▼
Analyze Question
  │
  ▼
Need Document Context?
  │
  ├───────────────┐
  │ YES           │ NO
  ▼               ▼
Retrieve         General
Context          Response
  │               │
  └───────┬───────┘
          ▼
       Generate
        Answer
          │
          ▼
         END
```

This makes it easier to extend the application later with additional tools and agentic behavior.

---

# 🔐 Environment Variables

API keys should **never be committed to GitHub**.

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Make sure `.env` is included in `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

# 📦 Dependencies

The project uses packages including:

```text
langchain
langgraph
llama-index
llama-index-embeddings-huggingface
langchain-google-genai
pymupdf
python-dotenv
```

The exact installed versions are stored in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# 🧪 Example

Suppose the PDF contains:

```text
An operating system acts as an intermediary between
the user and computer hardware.

The primary objective of an operating system is
to provide convenience to the user.
```

User:

```text
What is the primary objective of an operating system?
```

Retriever:

```text
The primary objective of an operating system is
to provide convenience to the user.
```

The future LLM layer will use this retrieved context to generate a natural-language answer.

---

# 🎯 Project Goals

The main goal of this project is to understand how modern AI applications can combine multiple frameworks instead of relying on a single library.

The project focuses on:

* Retrieval-Augmented Generation (RAG)
* Vector search
* Embeddings
* Document processing
* LLM integration
* Agent workflows
* Conditional routing
* AI application architecture

---

# 🔮 Future Improvements

Planned improvements include:

* [ ] Connect LlamaIndex retrieval to LangGraph
* [ ] Integrate LangChain with Gemini
* [ ] Generate final answers using retrieved context
* [ ] Add conversation memory
* [ ] Add source/page references to answers
* [ ] Support multiple PDFs
* [ ] Add PDF upload interface
* [ ] Add Streamlit web UI
* [ ] Add chat history
* [ ] Add document summarization
* [ ] Add question classification
* [ ] Add persistent vector database
* [ ] Add evaluation for RAG responses
* [ ] Deploy the application

---

# 📊 Why Use Three Frameworks?

This project intentionally demonstrates how the frameworks can complement each other.

### LlamaIndex

Used for the **data layer**:

```text
Documents
   ↓
Indexing
   ↓
Retrieval
```

### LangGraph

Used for the **workflow layer**:

```text
State
 ↓
Decision
 ↓
Tool
 ↓
Next State
```

### LangChain

Used for the **LLM layer**:

```text
Prompt
 ↓
LLM
 ↓
Response
```

This separation makes the application easier to understand and extend.

---

# 🔒 Security

Never commit sensitive information such as:

* API keys
* Passwords
* Access tokens
* Private documents
* `.env` files

Use:

```text
.env
```

for secrets and add it to:

```text
.gitignore
```

---

# 🤝 Contributing

Contributions and improvements are welcome.

To contribute:

```bash
git clone https://github.com/shahsurajdukhan/Study-Agent-Using-PDF.git
cd Study-Agent-Using-PDF
```

Create a new branch:

```bash
git checkout -b feature/new-feature
```

Make your changes, commit them:

```bash
git add .
git commit -m "Add new feature"
```

Push the branch:

```bash
git push origin feature/new-feature
```

Then open a Pull Request.

---

# 📄 License

This project is intended for educational and portfolio purposes.

You can add a specific open-source license such as MIT later if you want to make the project's licensing terms explicit.

---

# 👨‍💻 Author

**Suraj Shah**

Computer Science & Engineering Student

GitHub: [@shahsurajdukhan](https://github.com/shahsurajdukhan)

---

## ⭐ If You Find This Project Useful

Consider giving the repository a ⭐ on GitHub!

---

### 📌 Project Status

**Current stage:**

```text
✅ Python project setup
✅ Virtual environment
✅ LlamaIndex setup
✅ PDF processing
✅ PyMuPDF text extraction
✅ Hugging Face embeddings
✅ LlamaIndex vector index
✅ Document retrieval
✅ Initial LangGraph workflow
⬜ LangChain + Gemini integration
⬜ Complete agent workflow
⬜ Chat interface
⬜ Deployment
```

The project is being developed incrementally to demonstrate the complete pipeline from **PDF → Retrieval → Agent Workflow → LLM → Answer**.
