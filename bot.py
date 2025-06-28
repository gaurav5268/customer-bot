import threading
import datetime
import time
import re
import requests
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import streamlit as st
from rag_resource import get_similar_answer  # This should return top answer string from retriever

# ========== FLASK BACKEND API SETUP ========== #
app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
collection = client["complaintDB"]["complaints"]

@app.route('/complaints', methods=['POST'])
def create_complaint_api():
    data = request.json
    required = ['name', 'phone_number', 'email', 'complaint_details']
    if not all(k in data for k in required):
        return jsonify({"error": "Missing fields"}), 400

    data["created_at"] = datetime.datetime.now()
    result = collection.insert_one(data)
    return jsonify({
        "complaint_id": str(result.inserted_id),
        "message": "Complaint created successfully"
    }), 201

@app.route('/complaints/<complaint_id>', methods=['GET'])
def get_complaint_api(complaint_id):
    try:
        complaint = collection.find_one({"_id": ObjectId(complaint_id)})
        if complaint:
            complaint["_id"] = str(complaint["_id"])
            complaint["created_at"] = str(complaint["created_at"])
            complaint["complaint_id"] = complaint.pop("_id")
            return jsonify(complaint), 200
        else:
            return jsonify({"error": "Not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def run_flask_api():
    app.run(debug=False, use_reloader=False)


# ========== UTILITY FUNCTIONS ========== #
def create_complaint(payload):
    try:
        res = requests.post("http://127.0.0.1:5000/complaints", json=payload)
        return res.json().get("complaint_id", "Error")
    except Exception as e:
        return str(e)

def fetch_complaint_by_id(text):
    # Look for a 24-character MongoDB ObjectId in the text
    match = re.search(r'\b([a-fA-F0-9]{24})\b', text)
    if match:
        complaint_id = match.group(1)
        try:
            res = requests.get(f"http://127.0.0.1:5000/complaints/{complaint_id}")
            if res.status_code == 200:
                return res.json()
        except Exception:
            return None
    return None

def is_complaint_query(text):
    keywords = ["complaint", "file", "raise", "problem", "issue", "report"]
    return any(k in text.lower() for k in keywords)


# ========== STREAMLIT UI ========== #
def launch_streamlit_ui():
    st.set_page_config(page_title="Customer Support Chatbot", page_icon="🤖")
    st.title("🤖 Customer Support Chatbot")

    if "session" not in st.session_state:
        st.session_state.session = {}

    user_input = st.chat_input("Type your message...")

    if user_input:
        st.chat_message("user").write(user_input)
        session = st.session_state.session

        # Check if input contains complaint ID
        complaint_data = fetch_complaint_by_id(user_input)
        if complaint_data:
            formatted = "\n".join([f"**{k.capitalize()}**: {v}" for k, v in complaint_data.items()])
            st.chat_message("bot").markdown(f"📄 Complaint Details:\n\n{formatted}")
            return

        # Complaint registration flow
        if session.get("step") == "details":
            session["details"] = user_input
            session["step"] = "name"
            st.chat_message("bot").write("🧑 Your name?")
            return

        if session.get("step") == "name":
            session["name"] = user_input
            session["step"] = "phone"
            st.chat_message("bot").write("📞 Your phone number?")
            return

        if session.get("step") == "phone":
            session["phone_number"] = user_input
            session["step"] = "email"
            st.chat_message("bot").write("📧 Your email?")
            return

        if session.get("step") == "email":
            session["email"] = user_input
            payload = {
                "name": session["name"],
                "phone_number": session["phone_number"],
                "email": session["email"],
                "complaint_details": session["details"]
            }
            cid = create_complaint(payload)
            st.chat_message("bot").write(f"✅ Complaint registered! Complaint ID: {cid}")
            st.session_state.session = {}  # reset
            return

        if is_complaint_query(user_input):
            session["step"] = "details"
            st.chat_message("bot").write("📝 Please describe your issue.")
            return

        # Otherwise: get RAG answer
        response = get_similar_answer(user_input)
        if not response or "sorry" in response.lower():
            session["step"] = "details"
            session["details"] = user_input
            st.chat_message("bot").write("🤖 I couldn’t help with that. Let’s file a complaint. Describe your issue.")
        else:
            st.chat_message("bot").write(response)


# ========== MAIN ENTRY ========== #
if __name__ == "__main__":
    threading.Thread(target=run_flask_api, daemon=True).start()
    time.sleep(1.5)  # Give Flask a second to boot
    launch_streamlit_ui()
