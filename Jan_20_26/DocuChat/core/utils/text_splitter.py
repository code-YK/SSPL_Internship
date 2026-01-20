from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List

def split_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[str]:
    '''Split the input text into smaller chunks using RecursiveCharacterTextSplitter.'''

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = text_splitter.split_text(text)
    return chunks

