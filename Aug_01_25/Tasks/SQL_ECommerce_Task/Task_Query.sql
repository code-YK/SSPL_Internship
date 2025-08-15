<<<<<<< HEAD
-- List the top 10 customers by total spend.
SELECT  c.name, 
        c.email, 
        SUM(o.total_amount) AS total_spend,
        RANK() OVER (ORDER BY SUM(o.total_amount) DESC) AS rank_amt
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
LIMIT 10; 



-- Generate a report of daily revenue and order count for the last 30 days.
SELECT 
    DATE(order_date) AS order_date,
    COUNT(order_id) AS order_count,
    SUM(total_amount) AS total_revenue
FROM orders
WHERE order_date >= CURDATE() - INTERVAL 30 DAY
GROUP BY DATE(order_date)
ORDER BY DATE(order_date) DESC;



-- Identify most sold products in the last 3 months.
SELECT 
    p.name AS product_name,
    SUM(oi.quantity) AS total_quantity_sold,
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.order_id IN (
    SELECT order_id 
    FROM orders 
    WHERE order_date >= DATE('2024-07-31') - INTERVAL 3 MONTH
)
GROUP BY p.product_id
ORDER BY total_quantity_sold DESC;



-- Show total revenue broken down by product category.
SELECT 
    p.category,
    SUM(oi.price * oi.quantity) AS total_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;
=======
-- List the top 10 customers by total spend.
SELECT  c.name, 
        c.email, 
        SUM(o.total_amount) AS total_spend,
        RANK() OVER (ORDER BY SUM(o.total_amount) DESC) AS rank_amt
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
LIMIT 10; 



-- Generate a report of daily revenue and order count for the last 30 days.
SELECT 
    DATE(order_date) AS order_date,
    COUNT(order_id) AS order_count,
    SUM(total_amount) AS total_revenue
FROM orders
WHERE order_date >= CURDATE() - INTERVAL 30 DAY
GROUP BY DATE(order_date)
ORDER BY DATE(order_date) DESC;



-- Identify most sold products in the last 3 months.
SELECT 
    p.name AS product_name,
    SUM(oi.quantity) AS total_quantity_sold,
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.order_id IN (
    SELECT order_id 
    FROM orders 
    WHERE order_date >= DATE('2024-07-31') - INTERVAL 3 MONTH
)
GROUP BY p.product_id
ORDER BY total_quantity_sold DESC;



-- Show total revenue broken down by product category.
SELECT 
    p.category,
    SUM(oi.price * oi.quantity) AS total_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;
>>>>>>> a095286 (Save local changes before pull)
