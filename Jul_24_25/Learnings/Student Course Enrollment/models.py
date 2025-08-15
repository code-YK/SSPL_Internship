from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

# Many-to-many association table
enrollments = Table(
    'enrollments', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    courses = relationship("Course", secondary=enrollments, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)

    students = relationship("Student", secondary=enrollments, back_populates="courses")
