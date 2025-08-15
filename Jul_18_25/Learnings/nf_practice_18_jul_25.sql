-- | StudentID | Name       | Course1   | Course2   | Instructor1 | Instructor2 |
-- |-----------|------------|-----------|-----------|-------------|-------------|
-- | 101       | Ravi Kumar | Math      | Physics   | Dr. Mehta   | Dr. Verma   |
-- | 102       | Anjali     | Chemistry | NULL      | Dr. Sharma  | NULL        |
 CREATE DATABASE nf_db;
 USE nf_db;
 CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50)
);
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    instructor VARCHAR(50)
);
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

INSERT INTO students (student_id, name) VALUES
(101, 'Ravi Kumar'),
(102, 'Anjali Sharma'),
(103, 'Amit Verma'),
(104, 'Priya Desai');

INSERT INTO courses (course_id, course_name, instructor) VALUES
(201, 'Mathematics', 'Dr. Mehta'),
(202, 'Physics', 'Dr. Verma'),
(203, 'Chemistry', 'Dr. Sharma'),
(204, 'Biology', 'Dr. Nair');

INSERT INTO enrollments (student_id, course_id) VALUES
(101, 201),  -- Ravi → Mathematics
(101, 202),  -- Ravi → Physics
(102, 203),  -- Anjali → Chemistry
(103, 201),  -- Amit → Mathematics
(103, 204),  -- Amit → Biology
(104, 202);  -- Priya → Physics

