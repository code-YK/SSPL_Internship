from db import Session
from models import Student, Course

session = Session()

# Create students and courses
s1 = Student(name="Kuldeep")
s2 = Student(name="Vedant")

c1 = Course(title="Math")
c2 = Course(title="Physics")

# Enroll students
s1.courses.append(c1)
s1.courses.append(c2)
s2.courses.append(c1)

session.add_all([s1, s2, c1, c2])
session.commit()

# Query enrolled courses
students = session.query(Student).all()
for student in students:
    print(f"{student.name} is enrolled in: {[course.title for course in student.courses]}")
