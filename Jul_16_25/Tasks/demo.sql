-- Create a new database
CREATE DATABASE company_db;

-- Use the database (for MySQL)
USE company_db;

-- Create tables
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Insert data
INSERT INTO departments VALUES (1, 'HR'), (2, 'IT');
INSERT INTO employees VALUES (101, 'kuldeep', 1), (102, 'vedant', 2);

-- Select query
SELECT * FROM employees;
SELECT name FROM employees WHERE dept_id = 2;

-- Update query
UPDATE employees SET name = 'Robert' WHERE emp_id = 102;

-- Delete query
DELETE FROM employees WHERE emp_id = 101;
