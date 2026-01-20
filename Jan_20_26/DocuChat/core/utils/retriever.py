from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from config.settings import EMBEDDING_MODEL_NAME
from typing import List

def create_vector_store(doc_chunks: List[str]) -> FAISS:
    '''Create a FAISS vector store from the given documents using HuggingFace embeddings.'''

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vector_store = FAISS.from_documents(doc_chunks, embeddings)
    return vector_store