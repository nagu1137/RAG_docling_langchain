# RAG Pipeline with Docling & LangChain

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

---

## Table of Contents

- [Overview](#overview)
- [Project Diagram](#project-diagram)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Directory Layout](#directory-layout)
- [Dependencies](#dependencies)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This repository provides a **Retrieval‑Augmented Generation (RAG)** pipeline that leverages **Docling** for document parsing, **LangChain** for orchestration, and **Qdrant** as a vector store. The pipeline is designed to ingest PDF documents (e.g., HR policies) and answer natural‑language queries against the extracted knowledge.

---

## Project Diagram

> **Placeholder** – Insert a high‑level architecture diagram here (e.g., `docs/diagram.png`).

```mermaid
flowchart LR
    A[Document (PDF)] --> B[Docling Parser]
    B --> C[Hierarchical Chunker]
    C --> D[Embedding Model]
    D --> E[Qdrant Vector Store]
    E --> F[LangChain Retriever]
    F --> G[Groq LLM]
    G --> H[Answer]
```

---

## Prerequisites

- **Operating System**: Windows 10/11 (the provided `setup.bat` is Windows‑specific). Linux/macOS users can run the commands manually.
- **Python**: 3.10 or newer.
- **Git**: To clone the repository.

---

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your‑org/your‑repo.git
   cd your‑repo
   ```

2. **Run the initial setup script** (only the first time). This script creates a virtual environment, upgrades `pip`, and installs the required packages listed in `requirements.txt`.
   ```bash
   setup.bat
   ```
   > **Note**: `setup.bat` is a Windows batch file. On Linux/macOS, execute the equivalent commands manually:
   ```bash
   python -m venv .venv
   .venv/bin/pip install --upgrade pip
   .venv/bin/pip install -r requirements.txt
   ```

3. **Activate the virtual environment**
   - **Command Prompt**:
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **PowerShell**:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **Git Bash / Linux / macOS**:
     ```bash
     source .venv/Scripts/activate   # or source .venv/bin/activate on macOS/Linux
     ```

---

## Usage

### 1. Ingest a document and query it in a single step
```bash
python rag_pipeline.py --document "AtliqAI_HR_Policies.pdf" --query "What is the probation period?"
```

### 2. Query an existing vector store
```bash
python rag_pipeline.py --query "What is the policy on casual leaves?"
```

The script expects the **Groq API key** to be available as an environment variable (`GROQ_API_KEY`). See the *Environment Variables* section for details.

---

## Directory Layout

```
├── README.md                 # This file (project documentation)
├── Readme.txt                # Legacy readme (kept for reference)
├── rag_pipeline.py           # Main entry point for the RAG pipeline
├── requirements.txt          # Python dependencies
├── setup.bat                 # Windows‑only bootstrap script
├── .env.example              # Example environment file (do not commit actual keys)
└── docs/
    └── diagram.png           # Project diagram (optional)
```

---

## Dependencies

The project relies on the following Python packages (versions are managed via `requirements.txt`). If you need explicit version numbers, pin them in the file, e.g., `qdrant-client==1.6.0`.

- `qdrant-client`
- `sentence-transformers`
- `docling`
- `docling-core`
- `groq`
- `langchain-core`
- `langchain-groq`
- `langchain-huggingface`
- `langchain-qdrant`
- `huggingface-hub`

---

## Environment Variables

Create a `.env` file in the project root (or set the variables in your shell) with the following content:

```dotenv
GROQ_API_KEY=your_actual_api_key_here
```

The pipeline reads `GROQ_API_KEY` at runtime. Using a `.env` file keeps secrets out of source control.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes with clear messages.
4. Open a pull request describing the changes.

---

## License

This project is licensed under the MIT License – see the `LICENSE` file for details.
