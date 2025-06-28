# rag_resource.py
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

DB_FAISS_PATH = "vectorstore/db_faiss"

print("🔄 Loading Embedding Model & FAISS Index...")
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load FAISS vector store
vectorstore = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 3})

print("✅ RAG retriever is ready.")

def get_similar_answer(query: str) -> str:
    # Direct query for better matching with answer-only chunks
    docs = retriever.invoke(query.strip())

    if not docs or not docs[0].page_content:
        return "Sorry, I couldn't find a suitable answer."

    return docs[0].page_content.strip()
