# 🤖 AI Knowledge Assistant

An AI-powered **Knowledge Assistant** that allows users to interact with their documents using natural language.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded documents and generate accurate, context-aware answers using a Large Language Model (LLM).

Instead of manually searching through long documents, users can simply ask questions and get answers based on the available knowledge base.

---

## ✨ Features

* 📄 **Document ingestion** — Add documents to the knowledge base.
* 🔍 **Semantic search** — Retrieve relevant document chunks based on the user's question.
* 🧠 **AI-powered answers** — Generate answers using an LLM.
* 📚 **RAG architecture** — Ground responses in the content of the provided documents.
* 💬 **Natural language interaction** — Ask questions conversationally.
* ⚡ **Fast API backend** — Backend implemented with FastAPI.
* 🗂️ **Document listing** — View available documents through the API.
* 🔌 **API-based architecture** — Can easily be connected to a web frontend.

---

## 🏗️ Architecture

The application follows a Retrieval-Augmented Generation pipeline:

```text
                 ┌──────────────────┐
                 │      User        │
                 │   asks a query   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   FastAPI API    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  Query Processing│
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Semantic Search  │
                 │ / Vector Store   │
                 └────────┬─────────┘
                          │
                   Relevant chunks
                          │
                          ▼
                 ┌──────────────────┐
                 │       LLM        │
                 │ Answer Generation│
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │      Answer      │
                 └──────────────────┘
```

### RAG Pipeline

1. Documents are loaded into the application.
2. Documents are split into smaller chunks.
3. Embeddings are generated for the chunks.
4. Embeddings are stored in a vector database/vector store.
5. The user submits a question.
6. The system searches for the most relevant chunks.
7. The retrieved context is provided to the LLM.
8. The LLM generates an answer based on the retrieved information.

---

## 🛠️ Tech Stack

| Technology        | Purpose                              |
| ----------------- | ------------------------------------ |
| **Python**        | Main programming language            |
| **FastAPI**       | Backend REST API                     |
| **LangChain**     | LLM/RAG orchestration                |
| **LLM**           | Answer generation                    |
| **Embeddings**    | Semantic representation of documents |
| **Vector Store**  | Similarity search                    |
| **Uvicorn**       | ASGI server                          |
| **Python-dotenv** | Environment variable management      |

---


# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-knowledge-assistant.git
cd ai-knowledge-assistant
```

Replace `YOUR_USERNAME` with your GitHub username.

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

If your project uses another LLM provider, add the corresponding API key instead.

### ⚠️ Important

Never commit your `.env` file to GitHub.

Make sure your `.gitignore` contains:

```text
.env
venv/
__pycache__/
*.pyc
```

---

# ▶️ Running the Application

Start the FastAPI server using:

```bash
uvicorn app.main:app --reload
```
Start the Streamlit app  using:

```bash
 streamlit run .\streamlit_app.py
```

# 🎯 Project Goal

The goal of this project is to build a practical AI assistant capable of transforming a collection of documents into an **interactive knowledge base**.

Rather than searching through documents manually, users can communicate with their knowledge base using natural language.

---


## ⭐ If you find this project useful

Consider giving the repository a ⭐ on GitHub!
