USE students_db;

CREATE TABLE students_info (
    roll_num INT PRIMARY KEY,
    first_name VARCHAR(25),
    last_name VARCHAR(25)
);

CREATE TABLE marks (
    roll_num INT,
    sub_id INT,
    sub_name VARCHAR(20),
    mark INT,
    FOREIGN KEY (roll_num) REFERENCES students_info(roll_num)
);

INSERT INTO students_info VALUES 
(1, 'Kuldeep', 'Yadav'),
(2, 'Vedant', 'Kalal'),
(3, 'Rahul', 'Patel'),
(4, 'Aarav', 'Singh');
INSERT INTO students_info VALUES (5, 'Test', 'Student');

INSERT INTO marks VALUES
(1, 101, 'Maths', 90),
(1, 102, 'Physics', 85),
(2, 101, 'Maths', 60),
(3, 101, 'Maths', 50),
(5, 101, 'Maths', 77);

-- inner join
SELECT s.roll_num, s.first_name, m.sub_name, m.mark
FROM students_info as s
INNER JOIN marks as m 
ON s.roll_num = m.roll_num;

-- left join
SELECT s.roll_num, s.first_name, m.sub_name, m.mark
FROM students_info as s
LEFT JOIN marks as m 
ON s.roll_num = m.roll_num;

-- right join 
SELECT s.roll_num, s.first_name, m.sub_name, m.mark
FROM students_info as s
RIGHT JOIN marks as m 
ON s.roll_num = m.roll_num;

-- full outer join
SELECT s.roll_num, s.first_name, m.sub_name, m.mark
FROM students_info as s
LEFT JOIN marks as m 
ON s.roll_num = m.roll_num
UNION
SELECT s.roll_num, s.first_name, m.sub_name, m.mark
FROM students_info as s
RIGHT JOIN marks as m 
ON s.roll_num = m.roll_num;

-- avg() function
SELECT roll_num, AVG(mark) AS avg_mark
FROM marks
GROUP BY roll_num;

-- max()
SELECT sub_name, MAX(mark) AS max_mark
FROM marks
GROUP BY sub_name;

-- min()
SELECT sub_name, MIN(mark) AS max_mark
FROM marks
GROUP BY sub_name;

-- sum()
SELECT roll_num, SUM(mark) AS Total_marks
FROM marks
GROUP BY roll_num;

-- count()
SELECT s.roll_num,s.first_name, COUNT(m.sub_id) AS subject_count
FROM students_info AS s
LEFT JOIN marks AS m 
ON s.roll_num = m.roll_num
GROUP BY s.roll_num;

