import os
import datetime
import pandas as pd

from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings


CSV_PATH = r"C:\Users\Gravity\Desktop\chatbot\data\serv.csv"  # Path to your CSV file
VECTOR_STORE_PATH = "vectorstore/db_faiss"

def load_answers_from_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        if "answer" not in df.columns:
            raise ValueError(" CSV must contain an 'answer' column.")
        
        answers = df["answer"].dropna().tolist()
        answers = [a.strip() for a in answers if len(str(a).strip()) > 20]
        print(f"Loaded {len(answers)} answers from CSV.")
        return answers
    except Exception as e:
        print(f" Failed to load CSV: {e}")
        return []

def get_embedding_model():
    try:
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        print("Embedding model loaded.")
        return embedding_model
    except Exception as e:
        print(f"Failed to load embedding model: {e}")
        return None

def build_and_save_faiss_index(answer_chunks, embedding_model, index_path=VECTOR_STORE_PATH):
    try:
        print("Building FAISS vector store...")
        documents = [Document(page_content=chunk, metadata={"source": "csv"}) for chunk in answer_chunks]

        db = FAISS.from_documents(documents, embedding_model)

        if os.path.exists(index_path):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            index_path = f"{index_path}_{timestamp}"

        db.save_local(index_path)
        print(f"Vector store saved at: {index_path}")
    except Exception as e:
        print(f"Error while saving FAISS index: {e}")

# ====== MAIN EXECUTION ======
if __name__ == "__main__":
    print("Loading answers from CSV...")
    answer_chunks = load_answers_from_csv(CSV_PATH)

    if answer_chunks:
        print("Sample Preview:")
        for i, chunk in enumerate(answer_chunks[:3]):
            print(f"\n🔹 Answer {i+1}:\n{chunk[:200]}...\n")

        embedding_model = get_embedding_model()
        if embedding_model:
            build_and_save_faiss_index(answer_chunks, embedding_model)
