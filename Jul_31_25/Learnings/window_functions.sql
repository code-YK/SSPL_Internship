CREATE DATABASE products_db;

USE products_db;

-- Product Table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

-- Sales Table
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(product_id),
    quantity INT,
    sale_date DATE
);

-- Insert into products
INSERT INTO products (product_name, category, price) VALUES
('Laptop A', 'Electronics', 75000.00),
('Laptop B', 'Electronics', 82000.00),
('Phone A', 'Electronics', 30000.00),
('Phone B', 'Electronics', 45000.00),
('Shampoo', 'Cosmetics', 250.00),
('Conditioner', 'Cosmetics', 300.00),
('Face Wash', 'Cosmetics', 200.00),
('Notebook', 'Stationery', 50.00),
('Pen', 'Stationery', 10.00);

-- Insert into sales
INSERT INTO sales (product_id, quantity, sale_date) VALUES
(1, 5, '2024-06-01'),
(2, 3, '2024-06-05'),
(3, 10, '2024-06-10'),
(4, 7, '2024-06-12'),
(5, 20, '2024-06-15'),
(6, 15, '2024-06-18'),
(7, 18, '2024-06-20'),
(8, 30, '2024-06-22'),
(9, 50, '2024-06-25'),
(1, 4, '2024-06-27'),
(2, 2, '2024-06-28'),
(3, 12, '2024-06-29');

-- max,min,avg
SELECT product_name, category, price,
       MAX(price) OVER (PARTITION BY category) AS max_price_in_category,
       MIN(price) OVER (PARTITION BY category) AS min_price_in_category,
       AVG(price) OVER (PARTITION BY category) AS avg_price_in_category
FROM products;

-- row number
SELECT product_name, category, price,
       ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) AS row_num
FROM products;

-- rank
SELECT product_name, category, price,
       RANK() OVER (PARTITION BY category ORDER BY price DESC) AS price_rank
FROM products;

-- dense rank
SELECT product_name, category, price,
       DENSE_RANK() OVER (PARTITION BY category ORDER BY price DESC) AS dense_price_rank
FROM products;

-- lead lag
SELECT product_name, category, price,
       LAG(price) OVER (PARTITION BY category ORDER BY price) AS previous_price,
       LEAD(price) OVER (PARTITION BY category ORDER BY price) AS next_price
FROM products;

-- first value and last value
SELECT product_name, category, price,
       FIRST_VALUE(price) OVER (PARTITION BY category ORDER BY price) AS cheapest,
       LAST_VALUE(price) OVER (
           PARTITION BY category ORDER BY price 
           ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
       ) AS costliest
FROM products;


