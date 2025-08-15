from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Replace credentials if needed
DATABASE_URL ="mysql+pymysql://root:learn%40mysql1@localhost/student_course_db"


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()
