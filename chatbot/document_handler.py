

import os
import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from PyPDF2 import PdfReader
from io import BytesIO

class DocumentHandler:
    """Loads documents and builds FAISS index safely."""
    def __init__(self, docs_folder="docs"):
        self.docs_folder = docs_folder
        os.makedirs(self.docs_folder, exist_ok=True)
        self.new_docs = []  # store uploaded texts temporarily

    def load_documents(self):
        """Load all TXT and PDF documents from folder."""
        docs = []
        if not os.path.exists(self.docs_folder):
            st.warning(f"Docs folder '{self.docs_folder}' does not exist.")
            return docs

        for file in os.listdir(self.docs_folder):
            file_path = os.path.join(self.docs_folder, file)
            try:
                if file.endswith(".txt"):
                    try:
                        docs.extend(TextLoader(file_path, encoding="utf-8").load())
                    except UnicodeDecodeError:
                        docs.extend(TextLoader(file_path, encoding="latin-1").load())
                elif file.endswith(".pdf"):
                    docs.extend(PyPDFLoader(file_path).load())
            except Exception as e:
                st.warning(f"Failed to load '{file_path}': {e}")
                continue

        # Include uploaded files (not yet saved)
        docs.extend(self.new_docs)
        return docs

    def _extract_text_from_pdf_stream(self, file_stream):
        """Extract text from uploaded PDF stream (BytesIO)."""
        try:
            reader = PdfReader(file_stream)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            st.error(f"Failed to read PDF: {e}")
            return ""

    def add_document_text(self, filename, text):
        """Add uploaded file text to temporary storage for FAISS."""
        from langchain.docstore.document import Document
        self.new_docs.append(Document(page_content=text, metadata={"source": filename}))

    def build_faiss(self):
        """Build FAISS vector store from all documents."""
        docs = self.load_documents()
        if not docs:
            st.warning("No documents loaded. Please add files to the docs folder.")
            return None

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        split_docs = splitter.split_documents(docs)

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        try:
            self.vector_store = FAISS.from_documents(split_docs, embeddings)
            st.success("FAISS index built successfully!")
            return self.vector_store
        except Exception as e:
            st.error(f"Failed to build vector store: {e}")
            return None



