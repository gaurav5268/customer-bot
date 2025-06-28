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



Only the **answers** are embedded to improve semantic search relevance in the RAG pipeline.

---

## ⚙️ How It Works

- `memory.py`  
  - Reads Q&A pairs from `serv.csv`, extracts answers, generates embeddings using `MiniLM`, and stores them in FAISS.

- `rag_resource.py`  
  - Loads the FAISS vector index and initializes a retriever for semantic similarity-based responses.

- `bot.py`  
  - A Streamlit app that:
    - Handles user inputs.
    - Detects if the user is raising a complaint, tracking one, or asking a question.
    - Registers complaints via API, fetches details, or retrieves a relevant answer using RAG.

- `api.py`  
  - A Flask backend that:
    - Accepts new complaint data and stores it in MongoDB.
    - Retrieves complaint details using MongoDB `ObjectId`.

---

## 🚀 Steps to Run the Project Locally

### Step 1: Clone the Project Repository

git clone https://github.com/gaurav5268/customer-bot.git
cd customer-bot

## 🚀 Steps to Run the Project

### ✅ Step 2: Install Required Packages

pip install -r requirements.txt

Step 2: Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
Step 3: Ensure MongoDB Is Running
Make sure MongoDB is installed and running at localhost:27017.

Step 4: Build the Vector Database
bash
Copy
Edit
python memory.py
Step 5: Start the Chatbot Interface
bash
Copy
Edit
python bot.py
This will launch the chatbot interface in your browser using Streamlit.

📦 Required Python Packages
nginx
Copy
Edit
streamlit  
flask  
pymongo  
requests  
langchain  
sentence-transformers  
faiss-cpu
Generate the requirements file using:

bash
Copy
Edit
pip freeze > requirements.txt
🌱 Future Improvements
User/admin authentication

Email notifications for complaints

Enhanced chatbot memory with longer context

Dockerized deployment

Hosting with MongoDB Atlas + Streamlit Cloud

📄 License
This project is licensed under the MIT License and is free for educational or commercial use.

🙏 Acknowledgements
LangChain

HuggingFace Transformers

Facebook FAISS

Streamlit and Flask

yaml
Copy
Edit

---

### ✅ What To Do Next:
1. Create a file in your repo called `README.md`
2. Paste this content into it
3. Commit and push

Let me know if you'd like me to generate a `requirements.txt` file or a project d
