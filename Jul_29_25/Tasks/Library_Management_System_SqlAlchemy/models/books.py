from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    author = Column(String(50), nullable=False)
    total_copies = Column(Integer, nullable=False)
    available_copies = Column(Integer, nullable=False)

    transactions = relationship("Transaction", back_populates="books")

    def __init__(self, title, author, total_copies, available_copies=None):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies if available_copies is not None else total_copies

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author}, available_copies={self.available_copies})>"