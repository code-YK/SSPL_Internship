from langchain_community.document_loaders import PyPDFLoader
from typing import List
from langchain_core.documents import Document

def load_pdf(file_path: str) -> List[Document]:
    '''Load a PDF file and return its content as a list of LangChain Documents.'''

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    return documents

