
import streamlit as st
from pypdf import PdfReader
from docx import Document
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv

load_dotenv()
import uuid

# CONFIG 
st.set_page_config(page_title="RAG Chat App", layout="wide")
st.title("📄 RAG Chat App (Chat + Pinecone)")

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
try:
    if not PINECONE_API_KEY:
        PINECONE_API_KEY = st.secrets.get("PINECONE_API_KEY") if hasattr(st, "secrets") else None
except Exception:
    PINECONE_API_KEY = None

if not PINECONE_API_KEY:
    st.error("Pinecone API key not found. Set the `PINECONE_API_KEY` environment variable or add it to `.streamlit/secrets.toml`.")
    st.stop()

# Embedding Model 
@st.cache_resource
def load_embedder():
    return SentenceTransformer("all-MiniLM-L6-v2")

embedder = load_embedder()

# Pinecone Setup 
@st.cache_resource
def load_pinecone():
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index_name = "rag-chat-index"

    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
    return pc.Index(index_name)

index = load_pinecone()

# Session State 
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Helpers 
def read_pdf(file):
    reader = PdfReader(file)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def read_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def read_txt(file):
    return file.read().decode("utf-8")

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

# Sidebar 
st.sidebar.header("📂 Document Upload")
uploaded_files = st.sidebar.file_uploader(
    "Upload PDF, TXT, DOCX",
    type=["pdf", "txt", "docx"],
    accept_multiple_files=True
)

if uploaded_files and st.sidebar.button("Process Documents"):
    with st.spinner("Embedding & uploading to Pinecone..."):
        for file in uploaded_files:
            if file.type == "application/pdf":
                text = read_pdf(file)
            elif file.type == "text/plain":
                text = read_txt(file)
            else:
                text = read_docx(file)

            chunks = chunk_text(text)
            embeddings = embedder.encode(chunks).tolist()

            vectors = []
            for chunk, emb in zip(chunks, embeddings):
                vectors.append(
                    (
                        str(uuid.uuid4()),
                        emb,
                        {"text": chunk, "source": file.name}
                    )
                )

            index.upsert(vectors=vectors)

    st.sidebar.success("Documents indexed in Pinecone!")

if st.sidebar.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

# Chat Display 
st.subheader("Chat")

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# Chat Input 
query = st.chat_input("Ask a question from your documents...")

if query:
    st.session_state.chat_history.append({"role": "user", "content": query})

    with st.chat_message("assistant"):
        with st.spinner("Searching documents..."):
            query_embedding = embedder.encode(query).tolist()

            search_result = index.query(
                vector=query_embedding,
                top_k=3,
                include_metadata=True
            )

            contexts = [
                f"**Source:** {match['metadata']['source']}\n{match['metadata']['text']}"
                for match in search_result["matches"]
            ]

            answer = "\n\n---\n\n".join(contexts)
            st.markdown(answer)

    st.session_state.chat_history.append({"role": "assistant", "content": answer})










