from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_path = "sqlite:///E:/SSPL_Internship_Repo/Nov_11_25/Corporate_HR_Management_System/database/hr_management.db"

engine = create_engine(db_path)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()