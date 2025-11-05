USE employee_management;

-- 1. Employees in Finance or Sales departments
SELECT e.first_name, e.last_name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_name IN ('Finance', 'Sales');

-- 2. Employees with salary between 50k and 70k
SELECT first_name, last_name, salary
FROM employees
WHERE salary BETWEEN 50000 AND 70000;

-- 3. Employees sorted by highest salary first (top 3 employees)
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;

-- 4. Full name as Employee_Name + department name
SELECT CONCAT(first_name, ' ', last_name) AS Employee_Name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- 5. Project duration in days
SELECT proj_name,
       DATEDIFF(end_date, start_date) AS Project_Duration
FROM projects;

-- 6. Average and MAximum salary per department
SELECT d.dept_name, 
	AVG(e.salary) AS Avg_Salary,
    MAX(e.salary) AS Max_Salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY Avg_Salary DESC;

-- 7. Number of employees in each department
SELECT d.dept_name, COUNT(e.emp_id) AS Total_Employees
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;

-- 8. Employees working in Pune with salary > 60k, hired after 2021
SELECT e.first_name, e.last_name, e.salary, e.hire_date, d.location
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE d.location = 'Pune'
  AND e.salary > 60000
  AND e.hire_date > '2021-01-01'
ORDER BY e.salary DESC;

-- 9. Project -> Department > Employees assigned
SELECT p.proj_name, d.dept_name, CONCAT(e.first_name," ",e.last_name) AS employee_name 
FROM projects p
JOIN departments d ON p.dept_id = d.dept_id
JOIN employee_projects ep ON p.proj_id = ep.proj_id
JOIN employees e ON ep.emp_id = e.emp_id
ORDER BY d.dept_name, p.proj_name;

-- 10. Total employees assigned to each project
SELECT p.proj_name, COUNT(ep.emp_id) AS Total_Assigned
FROM projects p
LEFT JOIN employee_projects ep ON p.proj_id = ep.proj_id
GROUP BY p.proj_name;

-- 11️. Average salary of employees working on each project
SELECT p.proj_name, ROUND(AVG(e.salary), 2) AS Avg_Salary
FROM projects p
JOIN employee_projects ep ON p.proj_id = ep.proj_id
JOIN employees e ON ep.emp_id = e.emp_id
GROUP BY p.proj_name;

-- 12. Department name, project name, and number of employees per project
SELECT d.dept_name, p.proj_name, COUNT(ep.emp_id) AS Employee_Count
FROM departments d
JOIN projects p ON d.dept_id = p.dept_id
LEFT JOIN employee_projects ep ON p.proj_id = ep.proj_id
GROUP BY d.dept_name, p.proj_name
ORDER BY d.dept_name, Employee_Count DESC;

-- 13. Rank employees based on salary (overall)
SELECT emp_id, first_name, last_name, salary,
       RANK() OVER (ORDER BY salary DESC) AS Salary_Rank
FROM employees;

-- 14. Rank employees within their department
SELECT e.emp_id, e.first_name, e.last_name, d.dept_name, e.salary,
       RANK() OVER (PARTITION BY d.dept_name ORDER BY e.salary DESC) AS Dept_Rank
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- 15. Department-wise average salary shown for each employee
SELECT e.first_name, e.last_name, d.dept_name, e.salary,
       ROUND(AVG(e.salary) OVER (PARTITION BY d.dept_name), 2) AS Dept_Avg_Salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- 16. List top 2 highest-paid employees from each department
SELECT *
FROM (
    SELECT e.emp_id, e.first_name, e.last_name, d.dept_name, e.salary,
           DENSE_RANK() OVER (PARTITION BY d.dept_name ORDER BY e.salary DESC) AS rnk
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
) ranked
WHERE rnk <= 2;

