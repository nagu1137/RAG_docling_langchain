# RAG Pipeline with Docling & LangChain

## Project Overview

This repository provides a **Retrieval‑Augmented Generation (RAG) pipeline** that combines the power of **Docling** for document parsing and **LangChain** for building LLM‑driven applications.  The pipeline extracts text from PDFs, creates a vector store, and enables natural‑language queries over the content using large language models (LLMs) such as those provided by Groq.

The goal is to give developers a ready‑to‑run example that demonstrates how to:

- Load and chunk PDF documents.
- Embed the chunks into a vector database.
- Perform similarity search and generate answers with an LLM.
- Persist the vector store for future queries without re‑processing the source files.

## Setup Instructions

### Prerequisites

- **Windows**, **macOS**, or **Linux** with Python 3.9+ installed.
- An API key for the Groq service (or any other LLM provider you wish to use).

### First‑time Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your‑username/your‑repo.git
   cd your-repo
   ```
2. **Create a virtual environment and install dependencies**
   ```bash
   # Using the provided batch script (Windows) or the equivalent commands for Unix:
   ./setup.bat   # Windows only
   # Or manually:
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate.bat # Windows CMD
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. **Configure your Groq API key**
   ```bash
   # Windows (Command Prompt)
   set GROQ_API_KEY=your_actual_api_key_here
   # PowerShell
   $env:GROQ_API_KEY="your_actual_api_key_here"
   # macOS/Linux
   export GROQ_API_KEY=your_actual_api_key_here
   ```

### Subsequent Runs

After the initial setup you only need to activate the virtual environment and run the pipeline:
```bash
source .venv/bin/activate   # macOS/Linux
# or .venv\Scripts\activate.bat on Windows
python rag_pipeline.py --query "Your question here"
```

## Usage Examples

### 1. Ingest a PDF and query in a single command
```bash
python rag_pipeline.py \
    --document "AtliqAI_HR_Policies.pdf" \
    --query "What is the probation period?"
```

### 2. Query an already‑indexed document collection
```bash
python rag_pipeline.py --query "What is the policy on casual leaves?"
```

### 3. List available documents in the vector store
```bash
python rag_pipeline.py --list-documents
```

## Contribution Guidelines

We welcome contributions! Please follow these steps:

1. **Fork the repository** and create a new branch for your feature or bug‑fix.
2. **Write clear commit messages** and keep commits atomic.
3. **Add or update tests** where applicable.
4. **Update documentation** if you introduce new functionality.
5. **Submit a Pull Request** targeting the `main` branch. Ensure that the PR title is concise and the description explains the changes.

### Coding Style
- Follow **PEP 8** guidelines.
- Use type hints for public functions.
- Run `ruff` or `flake8` locally before committing.

### Testing
- Run the test suite with `pytest` (add tests under a `tests/` directory).
- Ensure that the pipeline works end‑to‑end with a sample PDF.

## License

This project is licensed under the **MIT License** – see the `LICENSE` file for details.

---

*Happy coding!*