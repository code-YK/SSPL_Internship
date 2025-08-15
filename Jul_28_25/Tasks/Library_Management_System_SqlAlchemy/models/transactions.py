from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from datetime import date

class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'),nullable=False)
    book_id = Column(Integer, ForeignKey('books.book_id'), nullable=False)
    issue_date = Column(String(50), nullable=False)
    return_date = Column(String(50), nullable=True)
    fine_amount = Column(Integer, nullable=True)

    users = relationship("User", back_populates="transactions")
    books = relationship("Book", back_populates="transactions")

    def __init__(self, user_id, book_id, issue_date=None, return_date=None, fine_amount=0):
        self.user_id = user_id
        self.book_id = book_id
        self.issue_date = issue_date if issue_date else date.today()
        self.return_date = return_date if return_date else None
        self.fine_amount = 0 if fine_amount is None else fine_amount

    def __repr__(self):
        return f"<Transaction(user_id={self.user_id}, book_id={self.book_id}, issue_date={self.issue_date})>"