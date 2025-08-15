CREATE DATABASE college_db;
USE college_db;

CREATE TABLE students(
	enr_id INT PRIMARY KEY,
    name VARCHAR(50),
    branch VARCHAR(50));

CREATE TABLE course(
	c_id INT PRIMARY KEY,
    enr_id INT,
    c_name VARCHAR(50),
    FOREIGN KEY (enr_id) REFERENCES students(enr_id));
    
INSERT INTO students (enr_id, name, branch) VALUES
(101, 'Ravi Kumar', 'Computer Science'),
(102, 'Anjali Sharma', 'Electronics'),
(103, 'Amit Verma', 'Mechanical'),
(104, 'Priya Desai', 'Electrical'),
(105, 'Rajesh Iyer', 'Civil'),
(106, 'Sneha Patel', 'Computer Science');

INSERT INTO course (c_id, enr_id, c_name) VALUES
(201, 101, 'Data Structures'),
(202, 101, 'Operating Systems'),
(203, 102, 'Digital Electronics'),
(204, 103, 'Thermodynamics'),
(205, 104, 'Circuit Theory'),
(206, 104, 'Power Systems');
-- No course for 105  and 106 

-- Inner Join 
SELECT s.enr_id, s.name, c.c_name
FROM students as s
INNER JOIN course as c
ON s.enr_id = c.enr_id ;

-- LEFT JOIN
SELECT s.enr_id, s.name, c.c_name
FROM students as s
LEFT JOIN course as c
ON s.enr_id = c.enr_id ;

-- RIGHT JOIN 
SELECT s.enr_id, s.name, c.c_name
FROM students as s
RIGHT JOIN course as c
ON s.enr_id = c.enr_id ;

-- FULL JOIN 
SELECT s.enr_id, s.name, c.c_name
FROM students as s
LEFT JOIN course as c
ON s.enr_id = c.enr_id
UNION
SELECT s.enr_id, s.name, c.c_name
FROM students as s
RIGHT JOIN course as c
ON s.enr_id = c.enr_id ;