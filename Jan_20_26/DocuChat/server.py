from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import os

from config.logger_config import setup_logger
logger = setup_logger(__name__)

from core.rag_pipeline import RAGPipeline

# Initialize FastAPI
app = FastAPI(title="DocuChat Backend")

# Constants
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
logger.info(f"Data directory set at: {DATA_DIR}")

# Initialize RAG Pipeline
rag_bot = RAGPipeline()

# Request Models
class ChatRequest(BaseModel):
    question: str

# In-memory state
conversation_history = []
current_document = None  

# POST /upload
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global current_document, conversation_history

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    # Ignore re-upload of same document
    if current_document == file.filename:
        logger.info("Same document uploaded again – skipping ingestion")
        return {"message": "File already processed"}

    file_path = os.path.join(DATA_DIR, file.filename)
    logger.info(f"Saving uploaded PDF to: {file_path}")

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Create vector store ONCE
    rag_bot.ingest_pdf(file_path)

    # Reset memory ONLY for new document
    conversation_history.clear()
    current_document = file.filename

    return {"message": "File processed successfully"}

# POST /chat
@app.post("/chat")
async def chat(request: ChatRequest):
    global conversation_history

    if not rag_bot.vector_store:
        raise HTTPException(
            status_code=400,
            detail="No document uploaded yet."
        )

    # Build conversation context
    history_text = ""
    for turn in conversation_history:
        history_text += f"User: {turn['question']}\nAssistant: {turn['answer']}\n"

    answer = rag_bot.chat(
        query=request.question,
        chat_history=history_text
    )

    conversation_history.append({
        "question": request.question,
        "answer": answer
    })

    return {"answer": answer}

# GET /health
@app.get("/health")
def health():
    logger.info("Health check requested")
    return {"status": "ok"}
