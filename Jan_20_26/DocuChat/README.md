# 📄 DocuChat – Chat with Your Documents

DocuChat is a **Retrieval-Augmented Generation (RAG)** application that allows you to upload PDF documents and interact with them through natural language conversations. It uses advanced AI models to understand your questions and provide accurate answers based on the document content.

## 🌟 Features

- **PDF Document Upload**: Upload and process PDF files for intelligent querying
- **Conversational AI**: Ask questions about your documents in natural language
- **Context-Aware Responses**: Maintains chat history for coherent conversations
- **Fast Retrieval**: Uses FAISS vector store for efficient similarity search
- **Modern UI**: Clean and intuitive Streamlit interface
- **RESTful API**: FastAPI backend for scalable deployments

## 🏗️ Architecture

The application follows a modular architecture:

```
DocuChat/
├── app.py                  # Streamlit frontend
├── server.py              # FastAPI backend server
├── config/                # Configuration modules
│   ├── llm_config.py     # LLM initialization
│   ├── settings.py       # Environment settings
│   └── logger_config.py  # Logging configuration
├── core/                  # Core RAG pipeline
│   ├── rag_pipeline.py   # Main RAG orchestration
│   └── utils/            # Utility functions
│       ├── pdf_loader.py       # PDF document loading
│       ├── text_splitter.py    # Document chunking
│       ├── retriever.py        # Vector store & retrieval
│       └── augmentation_prompt.py  # Prompt templates
├── data/                  # Uploaded PDFs storage
└── logs/                  # Application logs
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Groq API key (for LLM access)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd DocuChat
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   API_KEY=your_groq_api_key_here
   GROQ_MODEL=openai/gpt-oss-120b
   DEFAULT_TEMPERATURE=0.7
   DEBUG=False
   EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
   ```

### Running the Application

1. **Start the FastAPI backend server**
   ```bash
   uvicorn server:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`

2. **In a new terminal, start the Streamlit frontend**
   ```bash
   streamlit run app.py
   ```
   The app will open in your browser at `http://localhost:8501`

## 📖 Usage

1. **Upload a PDF**: Use the sidebar to upload your PDF document
2. **Wait for Processing**: The document will be split into chunks and indexed
3. **Ask Questions**: Type your questions in the chat input
4. **Get Answers**: Receive AI-generated answers based on document content

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `API_KEY` | Groq API key (required) | - |
| `GROQ_MODEL` | LLM model name | `openai/gpt-oss-120b` |
| `DEFAULT_TEMPERATURE` | LLM temperature (0-1) | `0.7` |
| `DEBUG` | Enable debug logging | `False` |
| `EMBEDDING_MODEL` | Embedding model for vector store | `sentence-transformers/all-MiniLM-L6-v2` |

### Supported Models

The application uses Groq for LLM inference. Popular models include:
- `openai/gpt-oss-120b`
- `mixtral-8x7b-32768`
- `llama-3.1-70b-versatile`
- `llama2-70b-4096`
- `gemma-7b-it`

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **LLM**: Groq API (ChatGroq)
- **Embeddings**: HuggingFace Sentence Transformers
- **Vector Store**: FAISS
- **PDF Processing**: LangChain Community (PyPDFLoader)
- **Text Splitting**: LangChain Recursive Character Text Splitter

## 📝 API Endpoints

### POST `/upload`
Upload and process a PDF document.

**Request**: Multipart form data with PDF file

**Response**:
```json
{
  "message": "File processed successfully"
}
```

### POST `/chat`
Send a question and receive an answer.

**Request**:
```json
{
  "question": "What is the main topic of the document?"
}
```

**Response**:
```json
{
  "answer": "The main topic is..."
}
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError` for imports
- **Solution**: Ensure you're in the project root directory and virtual environment is activated

**Issue**: API key error
- **Solution**: Check that your `.env` file contains a valid `API_KEY`

**Issue**: Model not found error
- **Solution**: Verify the `GROQ_MODEL` in your `.env` file is a valid Groq model name

**Issue**: Cannot connect to backend
- **Solution**: Ensure the FastAPI server is running on port 8000

## 📊 Logging

Logs are stored in the `logs/` directory:
- File: `logs/app.log`
- Rotation: 5 MB per file, 3 backup files
- Format: `YYYY-MM-DD HH:MM:SS || LEVEL || MODULE || MESSAGE`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📄 License

This project is open-source and available under the MIT License.

## 🙏 Acknowledgments

- LangChain for the RAG framework
- Groq for LLM API
- Streamlit for the frontend framework
- FastAPI for the backend framework

---

**Built with ❤️ using LangChain, FastAPI, and Streamlit**
