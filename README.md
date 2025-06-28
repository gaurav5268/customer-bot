# 🤖 Smart Customer Support Chatbot

A fully functional AI-powered chatbot that provides:
- Contextual answers using a **Retrieval-Augmented Generation (RAG)** pipeline
- A **complaint registration and tracking system** using **Flask + MongoDB**
- A **Streamlit-based chat UI** for real-time interaction

---

## 🚀 Features

✅ Answers user queries using custom knowledge base  
📝 Allows users to register and track complaints  
📄 Uses a lightweight Q&A CSV file as the data source  
🧠 Retrieval with HuggingFace sentence transformers + FAISS  
📦 Self-contained: No external APIs or LLMs required  
💬 Built with an intuitive Streamlit interface  

---

## 📁 Project Structure

CHATBOT/
├── api.py # Flask API for complaint handling
├── bot.py # Streamlit chatbot interface
├── memory.py # CSV embedding + FAISS vector store builder
├── rag_resource.py # Loads retriever & handles query matching
├── data/
│ ├── serv.csv # Customer support Q&A knowledge base
│ └── service.pdf # (optional, unused in current version)
├── vectorstore/ # Auto-generated FAISS index
└── pycache/ # Bytecode cache


---

## 🧩 Tech Stack

| Layer              | Technology                                           |
|--------------------|----------------------------------------------------- |
| Embedding Model    |sentence-transformers/all-MiniLM-L6-v2` (HuggingFace) |
| Vector Store       | FAISS (Facebook AI Similarity Search)                |
| RAG Framework      | LangChain                                            |
| Complaint Storage  | MongoDB (local instance)                             |
| Backend API        | Flask (RESTful)                                      |
| Frontend UI        | Streamlit Chat Interface                             |

---

## 📝 Dataset Format (serv.csv)

You define your support knowledge as:
Q: What is your return policy?
A: We accept returns within 30 days of delivery...

Q: how to track my order?
A: You can track using the link sent to your email...
