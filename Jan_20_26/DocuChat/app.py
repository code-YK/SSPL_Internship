import streamlit as st
import requests

# Configuration
API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="DocuChat",
    page_icon="📄",
    layout="wide"
)

st.title("📄 DocuChat – Chat with your Document")

# Session State
if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

if "file_uploaded" not in st.session_state:   
    st.session_state.file_uploaded = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar – Document Upload
with st.sidebar:
    st.header("📤 Upload Document")

    uploaded_file = st.file_uploader(
        "Upload a PDF file",
        type=["pdf"]
    )

    # Upload ONLY once
    if uploaded_file and not st.session_state.file_uploaded:
        with st.spinner("Uploading and processing document..."):
            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")
            }

            response = requests.post(
                f"{API_BASE_URL}/upload",
                files=files
            )

        if response.status_code == 200:
            st.success("Document uploaded and processed successfully ✅")
            st.session_state.document_uploaded = True
            st.session_state.file_uploaded = True
            st.session_state.chat_history = []
        else:
            st.error(response.json().get("detail", "Upload failed"))

# Chat Interface
st.subheader("💬 Chat Interface")

if not st.session_state.document_uploaded:
    st.info("Please upload a document from the sidebar to start chatting.")
else:
    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(message)

    user_question = st.chat_input("Ask a question about the document...")

    if user_question:
        st.session_state.chat_history.append(("user", user_question))
        with st.chat_message("user"):
            st.markdown(user_question)

        with st.spinner("Thinking..."):
            response = requests.post(
                f"{API_BASE_URL}/chat",
                json={"question": user_question}
            )

        answer = response.json().get("answer", "Something went wrong")

        st.session_state.chat_history.append(("assistant", answer))
        with st.chat_message("assistant"):
            st.markdown(answer)
