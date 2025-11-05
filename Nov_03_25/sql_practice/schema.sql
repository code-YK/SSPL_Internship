CREATE DATABASE employee_management;
USE employee_management;

-- 1. Departments Table
CREATE TABLE departments (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

-- 2. Employees Table
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    dept_id INT,
    salary DECIMAL(10,2),
    hire_date DATE,
    manager_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);

-- 3. Projects Table
CREATE TABLE projects (
    proj_id INT AUTO_INCREMENT PRIMARY KEY,
    proj_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- 4. Employee_Projects (Many-to-Many relationship)
CREATE TABLE employee_projects (
    emp_id INT,
    proj_id INT,
    hours_worked INT,
    PRIMARY KEY (emp_id, proj_id),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (proj_id) REFERENCES projects(proj_id)
);

-- 5. Attendance Table
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT,
    attendance_date DATE,
    status ENUM('Present','Absent','Leave') DEFAULT 'Present',
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);



INSERT INTO departments (dept_name, location)
VALUES
('HR', 'Mumbai'),
('Finance', 'Delhi'),
('Engineering', 'Bengaluru'),
('Sales', 'Pune'),
('Marketing', 'Hyderabad');

INSERT INTO employees (first_name, last_name, dept_id, salary, hire_date, manager_id)
VALUES
('Amit', 'Sharma', 3, 95000, '2020-01-10', NULL),
('Priya', 'Verma', 4, 72000, '2021-02-12', NULL),
('Rohan', 'Iyer', 5, 68000, '2020-11-05', NULL),
('Sneha', 'Patel', 3, 56000, '2021-04-22', 1),
('Karan', 'Reddy', 3, 61000, '2022-06-10', 1),
('Neha', 'Singh', 2, 50000, '2021-09-14', NULL),
('Vikram', 'Joshi', 1, 44000, '2022-01-20', NULL),
('Meera', 'Deshmukh', 4, 53000, '2021-08-02', 2),
('Arjun', 'Pillai', 5, 59000, '2022-02-16', 3),
('Lakshmi', 'Menon', 3, 64000, '2019-12-19', 1),
('Manish', 'Kapoor', 3, 76000, '2020-09-25', 1),
('Nisha', 'Bhatia', 5, 52000, '2022-04-10', 3),
('Om', 'Tripathi', 4, 47000, '2022-03-05', 2);

INSERT INTO projects (proj_name, start_date, end_date, dept_id)
VALUES
('Payroll Automation', '2022-01-01', '2022-06-30', 2),
('AI Traffic System', '2022-03-15', '2023-03-15', 3),
('Sales Tracker App', '2021-09-01', '2022-02-28', 4),
('Ad Campaign 2022', '2022-04-01', '2022-08-15', 5),
('Employee Wellness Program', '2022-02-01', '2022-12-31', 1);

INSERT INTO attendance (emp_id, attendance_date, status)
VALUES
(1, '2025-11-01', 'Present'),
(2, '2025-11-01', 'Present'),
(3, '2025-11-01', 'Leave'),
(4, '2025-11-01', 'Present'),
(5, '2025-11-01', 'Absent'),
(6, '2025-11-01', 'Present'),
(7, '2025-11-01', 'Present'),
(8, '2025-11-01', 'Present'),
(9, '2025-11-01', 'Leave'),
(10, '2025-11-01', 'Present');

INSERT INTO employee_projects (emp_id, proj_id, hours_worked)
VALUES
-- Finance Department (Payroll Automation)
(6, 1, 1500),
-- Engineering Department (AI Traffic System)
(1, 2, 1800),
(4, 2, 1600),
(5, 2, 1400),
(10, 2, 1200),
(11, 2, 1500),
-- Sales Department (Sales Tracker App)
(2, 3, 1700),
(8, 3, 1400),
(13, 3, 1000),
-- Marketing Department (Ad Campaign 2022)
(3, 4, 1600),
(9, 4, 1300),
(12, 4, 1200),
-- HR Department (Employee Wellness Program)
(7, 5, 1100);


