import os
import argparse
from docling.document_converter import DocumentConverter
from docling_core.transforms.chunker import HierarchicalChunker
from langchain_core.documents import Document
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_core.prompts import ChatPromptTemplate

# Configuration Constants
EMBED_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
VECTORSTORE_PATH = "/tmp/my_lang_vs"
COLLECTION_NAME = "hr_docs"

def convert_chunk(doc_chunk):
    """Converts a Docling DocChunk into a plain dict."""
    headings = doc_chunk.meta.headings or []
    content = doc_chunk.text.strip()
    breadcrumb = " > ".join(headings)
    chunk_text = f"{breadcrumb}\n\n{content}" if breadcrumb else content

    return {
        "headings": headings,
        "content": content,
        "chunk_text": chunk_text,
    }

def format_docs(docs):
    parts = []
    for i, doc in enumerate(docs, 1):
        parts.append(f"[{i}]: \n{doc.page_content}")
    return "\n\n---\n\n".join(parts)

def main():
    parser = argparse.ArgumentParser(description="RAG System with Docling Chunks and Qdrant Vector Store")
    parser.add_argument("--document", type=str, help="Path to the document to parse and ingest (optional)")
    parser.add_argument("--query", type=str, required=True, help="Question to ask the RAG system")
    args = parser.parse_args()

    # 1. Initialize Embeddings and LLM Components
    print("Initializing embedding model...")
    embedder = HuggingFaceEmbeddings(model_name=EMBED_MODEL_ID)
    
    print("Initializing Groq Language Model...")
    llm = ChatGroq(
        model="qwen/qwen3-32b",
        temperature=0,
        max_tokens=None,
        reasoning_format="parsed",
        timeout=None,
        max_retries=2,
    )

    # 2. Document Parsing and Vectorstore Ingestion (If a document is provided)
    if args.document:
        if not os.path.exists(args.document):
            print(f"Error: Document file '{args.document}' not found.")
            return

        print(f"Parsing document: {args.document} ...")
        converter = DocumentConverter()
        result = converter.convert(args.document)
        
        chunker = HierarchicalChunker()
        doc_chunks = list(chunker.chunk(result.document))
        
        chunks = [convert_chunk(c) for c in doc_chunks]
        
        docs = []
        for chunk in chunks:
            docs.append(
                Document(
                    page_content=chunk["chunk_text"],
                    metadata={"headings": chunk["headings"]}
                )
            )

        print("Building and saving vector store collection...")
        vectorstore = QdrantVectorStore.from_documents(
            documents=docs,
            embedding=embedder,
            path=VECTORSTORE_PATH,
            collection_name=COLLECTION_NAME,
        )
    else:
        # Load the existing local vector database directly
        print("Loading local vector store collection...")
        vectorstore = QdrantVectorStore.from_existing_collection(
            embedding=embedder,
            path=VECTORSTORE_PATH,
            collection_name=COLLECTION_NAME,
        )

    # 3. Setting up RAG workflow
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    
    RAG_PROMPT = ChatPromptTemplate.from_messages([
        ("system", "Answer using ONLY the context below. Cite section names. Say 'I don't know' if unsure."),
        ("human", "Context:\n{context}\n\nQuestion: {question}")
    ])

    print(f"Retrieving chunks for query: '{args.query}'")
    retrieved_docs = retriever.invoke(args.query)
    context = format_docs(retrieved_docs)
    
    prompt_value = RAG_PROMPT.invoke({"context": context, "question": args.query})
    
    print("Generating completion response...")
    response = llm.invoke(prompt_value)
    
    print("\n" + "="*40 + " RAG ANSWER " + "="*40)
    print(response.content)
    print("="*92)

if __name__ == "__main__":
    main()