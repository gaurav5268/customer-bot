# Customer Support Chatbot

A fully functional AI-powered chatbot that provides:
- Contextual answers using a **Retrieval-Augmented Generation (RAG)** pipeline
- A **complaint registration and tracking system** using **Flask + MongoDB**
- A **Streamlit-based chat UI** for real-time interaction

---

## Features

- Answers user queries using custom knowledge base  
- Allows users to register and track complaints  
- Uses a lightweight Q&A CSV file as the data source  
- Retrieval with HuggingFace sentence transformers + FAISS  
- Built with an intuitive Streamlit interface  

---

## Project Structure

CHATBOT/
- bot.py # Streamlit chatbot interface
- memory.py # CSV embedding + FAISS vector store builder
- rag_resource.py # Loads retriever & handles query matching
- data/
  - serv.csv # Customer support Q&A knowledge base
  - service.pdf # (optional, unused in current version)
- vectorstore/ # Auto-generated FAISS index
- pycache/ # Bytecode cache


--

## Tech Stack

| Layer              | Technology                                           |
|--------------------|----------------------------------------------------- |
| Embedding Model    |sentence-transformers/all-MiniLM-L6-v2` (HuggingFace) |
| Vector Store       | FAISS (Facebook AI Similarity Search)                |
| RAG Framework      | LangChain                                            |
| Complaint Storage  | MongoDB (local instance)                             |
| Backend API        | Flask (RESTful)                                      |
| Frontend UI        | Streamlit Chat Interface                             |

---

## Dataset Format (serv.csv)

You define your support knowledge as:
- Q: What is your return policy?
- A: We accept returns within 30 days of delivery...

- Q: how to track my order?
- A: You can track using the link sent to your email...



Note : Only the **answers** are embedded to improve semantic search relevance in the RAG pipeline.

---

##  How It Works

- `memory.py`  
  - Reads Q&A pairs from `serv.csv`, extracts answers, generates embeddings using `MiniLM`, and stores them in FAISS.

- `rag_resource.py`  
  - Loads the FAISS vector index and initializes a retriever for semantic similarity-based responses.

- `bot.py`
    - It act as interface (streamlit).
    - Handles user inputs.
    - Detects if the user is raising a complaint, tracking one, or asking a question.
    - Registers complaints via API, fetches details, or retrieves a relevant answer using RAG.
    - Retrieves complaint details using MongoDB `ObjectId`


---

## Steps to Run the Project Locally

### Step 1: Clone the Project Repository

git clone https://github.com/gaurav5268/customer-bot.git
cd customer-bot

## Steps to Run the Project

### Step 2: Install Required Packages

'pip install -r requirements.txt'

Step 3: Ensure MongoDB Is Running
Make sure MongoDB is installed and running at localhost:27017.

Step 4: Build the Vector Database
python memory.py

Step 5: Start the Chatbot Interface
python bot.py

This will launch the chatbot interface in your browser using Streamlit.

---

# Chatbot interface

 Streamlit chatbot interface is used to run the bot.
 ![image](https://github.com/user-attachments/assets/8745ab1d-cf2b-4503-958d-9f96bbe095ca)


## How data is stored

The complaints are stored in the connected MongoDB server/database which is connected like below and can be retrieve when needed.
![image](https://github.com/user-attachments/assets/cd41e964-15e1-462d-9f00-dfdf7f803d4a)


## Required Python Packages

streamlit  
flask  
pymongo  
requests  
langchain  
sentence-transformers  
faiss-cpu

Generate the requirements file using:

pip freeze > requirements.txt
## Future Improvements
User/admin authentication

Email notifications for complaints

Enhanced chatbot memory with longer context

Dockerized deployment

Hosting with MongoDB Atlas + Streamlit Cloud

# Acknowledgements
LangChain

HuggingFace Transformers

Facebook FAISS

Streamlit and Flask

