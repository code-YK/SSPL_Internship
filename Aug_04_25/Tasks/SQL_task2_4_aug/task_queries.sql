<<<<<<< HEAD
-- 1. Loyal Electronics Customers
-- Problem Statement: Find the names of customers who have purchased all the products in the 
-- 'Electronics' category.
SELECT c.name
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE p.category = 'Electronics'
GROUP BY c.id, c.name
HAVING COUNT(DISTINCT p.id) = (
    SELECT COUNT(*) FROM products WHERE category = 'Electronics'
);


-- 2. Above Average Sellers
-- Problem Statement: For each product category, find the names of products that sold more 
-- units than the average units sold per product in that category.

SELECT p.category, p.name
FROM products p
JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.category, p.id, p.name
HAVING SUM(oi.quantity) > (
    SELECT AVG(sub.total_quantity)
    FROM (
        SELECT SUM(oi2.quantity) AS total_quantity
        FROM products p2
        JOIN order_items oi2 ON p2.id = oi2.product_id
        WHERE p2.category = p.category
        GROUP BY p2.id
    ) sub
);

-- 3. Big Spenders
-- Problem Statement: Find the top 3 customers who spent the most. Total spend is calculated as 
-- quantity * price.

SELECT c.name 
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
DENSE_RANK() OVER (ORDER BY SUM(oi.quantity * oi.price) DESC) AS total_spend
LIMIT 3;

-- 4. Product Diversity Champs
-- Problem Statement: Find customer IDs and month (format YYYY-MM) where a customer 
-- purchased more than 3 distinct products
SELECT 
    o.customer_id,
    TO_CHAR(o.order_date, 'YYYY-MM') AS month,
    COUNT(DISTINCT oi.product_id) AS distinct_products
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.customer_id, TO_CHAR(o.order_date, 'YYYY-MM')
HAVING COUNT(DISTINCT oi.product_id) > 3;

-- 5. Unwanted Inventory
-- Problem Statement: Find the names of products that have never been ordered.
SELECT p.name
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
WHERE oi.product_id IS NULL;


-- 6. Category Clashes in Orders
-- Problem Statement: Find order IDs where an order contains more than one product from the 
-- same category.
SELECT o.id AS order_id
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
GROUP BY o.id, p.category
HAVING COUNT(DISTINCT oi.product_id) > 1;

-- 7. Category Bestsellers
-- Problem Statement: For each category, find the product(s) with the highest total quantity sold.
SELECT p.category, p.name, SUM(oi.quantity) AS total_quantity
FROM products p
JOIN order_items oi ON p.id = oi.product_id
DENSE_RANK OVER (PARTITION BY p.category ORDER BY SUM(oi.quantity) DESC) AS rank
HAVING rank = 1
=======
-- 1. Loyal Electronics Customers
-- Problem Statement: Find the names of customers who have purchased all the products in the 
-- 'Electronics' category.
SELECT c.name
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE p.category = 'Electronics'
GROUP BY c.id, c.name
HAVING COUNT(DISTINCT p.id) = (
    SELECT COUNT(*) FROM products WHERE category = 'Electronics'
);


-- 2. Above Average Sellers
-- Problem Statement: For each product category, find the names of products that sold more 
-- units than the average units sold per product in that category.

SELECT p.category, p.name
FROM products p
JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.category, p.id, p.name
HAVING SUM(oi.quantity) > (
    SELECT AVG(sub.total_quantity)
    FROM (
        SELECT SUM(oi2.quantity) AS total_quantity
        FROM products p2
        JOIN order_items oi2 ON p2.id = oi2.product_id
        WHERE p2.category = p.category
        GROUP BY p2.id
    ) sub
);

-- 3. Big Spenders
-- Problem Statement: Find the top 3 customers who spent the most. Total spend is calculated as 
-- quantity * price.

SELECT c.name 
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
DENSE_RANK() OVER (ORDER BY SUM(oi.quantity * oi.price) DESC) AS total_spend
LIMIT 3;

-- 4. Product Diversity Champs
-- Problem Statement: Find customer IDs and month (format YYYY-MM) where a customer 
-- purchased more than 3 distinct products
SELECT 
    o.customer_id,
    TO_CHAR(o.order_date, 'YYYY-MM') AS month,
    COUNT(DISTINCT oi.product_id) AS distinct_products
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.customer_id, TO_CHAR(o.order_date, 'YYYY-MM')
HAVING COUNT(DISTINCT oi.product_id) > 3;

-- 5. Unwanted Inventory
-- Problem Statement: Find the names of products that have never been ordered.
SELECT p.name
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
WHERE oi.product_id IS NULL;


-- 6. Category Clashes in Orders
-- Problem Statement: Find order IDs where an order contains more than one product from the 
-- same category.
SELECT o.id AS order_id
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
GROUP BY o.id, p.category
HAVING COUNT(DISTINCT oi.product_id) > 1;

-- 7. Category Bestsellers
-- Problem Statement: For each category, find the product(s) with the highest total quantity sold.
SELECT p.category, p.name, SUM(oi.quantity) AS total_quantity
FROM products p
JOIN order_items oi ON p.id = oi.product_id
DENSE_RANK OVER (PARTITION BY p.category ORDER BY SUM(oi.quantity) DESC) AS rank
HAVING rank = 1
>>>>>>> a095286 (Save local changes before pull)
GROUP BY p.category;