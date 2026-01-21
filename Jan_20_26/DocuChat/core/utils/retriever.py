from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from config.settings import EMBEDDING_MODEL_NAME
from typing import List

def create_vector_store(doc_chunks: List[str]) -> FAISS:
    '''Create a FAISS vector store from the given documents using HuggingFace embeddings.'''

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vector_store = FAISS.from_documents(doc_chunks, embeddings)
    return vector_store

def retrieve_similar_documents(vector_store: FAISS, query: str, k: int = 5) -> List[str]:
    '''Retrieve similar documents from the vector store based on the query.'''

    similar_docs = vector_store.similarity_search(query, k=k)
    return similar_docs

