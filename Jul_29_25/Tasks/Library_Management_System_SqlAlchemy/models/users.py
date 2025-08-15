from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from datetime import date

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    join_date = Column(String(50), nullable=False)

    transactions = relationship("Transaction", back_populates="users")

    def __init__(self, name, email, join_date):
        self.name = name
        self.email = email
        self.join_date = join_date

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"  
