<<<<<<< HEAD

INSERT INTO customers (name, email, created_at) VALUES
('Aarav Sharma', 'aarav.sharma@example.in', '2024-01-15'),
('Priya Iyer', 'priya.iyer@example.in', '2024-02-10'),
('Rohan Mehta', 'rohan.mehta@example.in', '2024-03-05'),
('Neha Reddy', 'neha.reddy@example.in', '2024-03-20'),
('Vikram Singh', 'vikram.singh@example.in', '2024-04-12'),
('Kavya Nair', 'kavya.nair@example.in', '2024-05-01'),
('Aditya Joshi', 'aditya.joshi@example.in', '2024-05-15'),
('Ishita Desai', 'ishita.desai@example.in', '2024-06-02'),
('Manish Agarwal', 'manish.agarwal@example.in', '2024-06-15'),
('Pooja Bhatia', 'pooja.bhatia@example.in', '2024-07-01'),
('Harshita Sinha', 'harshita.sinha@example.in', '2024-07-10'),
('Karan Verma', 'karan.verma@example.in', '2024-07-15'),
('Simran Kaur', 'simran.kaur@example.in', '2024-07-20'),
('Ankit Pandey', 'ankit.pandey@example.in', '2024-07-25'),
('Sneha Patil', 'sneha.patil@example.in', '2024-07-30');



INSERT INTO products (name, category, price) VALUES
('Tata Tea Gold', 'Beverages', 120.00),
('Aashirvaad Atta 5kg', 'Grocery', 280.00),
('Parle-G Biscuits', 'Snacks', 10.00),
('Dabur Honey 250g', 'Health', 199.00),
('Himalaya Face Wash', 'Personal Care', 150.00),
('Fortune Sunflower Oil 1L', 'Grocery', 140.00),
('Dettol Handwash', 'Household', 99.00),
('Amul Butter 500g', 'Dairy', 245.00),
('Samsung Galaxy M14', 'Electronics', 13999.00),
('Boat Rockerz 255', 'Electronics', 1299.00),
('Maggi 12-pack', 'Snacks', 96.00),
('Colgate Toothpaste 200g', 'Personal Care', 89.00),
('Lijjat Papad', 'Snacks', 85.00),
('Prestige Induction Cooker', 'Kitchen Appliances', 3499.00),
('Surf Excel 1kg', 'Household', 195.00);



INSERT INTO orders (customer_id, order_date, total_amount) VALUES
(1, '2024-04-15', 430.00),
(2, '2024-04-18', 389.00),
(3, '2024-04-20', 14299.00),
(4, '2024-04-25', 395.00),
(5, '2024-04-30', 154.00),
(6, '2024-05-03', 699.00),
(7, '2024-05-10', 138.00),
(8, '2024-06-06', 269.00),
(9, '2024-06-16', 344.00),
(10, '2024-06-25', 17000.00),
(11, '2024-07-03', 495.00),
(12, '2024-07-10', 102.00),
(13, '2024-07-18', 380.00),
(14, '2024-07-26', 1200.00),
(15, '2024-07-31', 550.00);


INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
-- Order 1
(1, 1, 2, 240.00),
(1, 3, 5, 50.00),
(1, 5, 1, 150.00),

-- Order 2
(2, 2, 1, 280.00),
(2, 7, 1, 99.00),

-- Order 3
(3, 9, 1, 13999.00),
(3, 10, 1, 1299.00),

-- Order 4
(4, 4, 1, 199.00),
(4, 8, 1, 245.00),

-- Order 5
(5, 6, 1, 140.00),
(5, 3, 1, 10.00),
(5, 7, 1, 99.00),

-- Order 6
(6, 11, 2, 192.00),
(6, 13, 1, 85.00),
(6, 5, 1, 150.00),
(6, 7, 1, 99.00),

-- Order 7
(7, 3, 10, 100.00),
(7, 12, 1, 89.00),

-- Order 8
(8, 2, 1, 280.00),
(8, 14, 1, 3499.00),

-- Order 9
(9, 6, 2, 280.00),
(9, 15, 1, 195.00),

-- Order 10
(10, 9, 1, 13999.00),
(10, 10, 2, 2598.00),
(10, 12, 1, 89.00),
(10, 5, 1, 150.00),

-- Order 11
(11, 1, 1, 120.00),
(11, 2, 1, 280.00),
(11, 7, 1, 99.00),

-- Order 12
(12, 3, 3, 30.00),
(12, 13, 1, 85.00),

-- Order 13
(13, 14, 1, 3499.00),
(13, 15, 1, 195.00),

-- Order 14
(14, 10, 1, 1299.00),
(14, 11, 1, 96.00),

-- Order 15
(15, 4, 2, 398.00),
(15, 8, 1, 245.00);
=======

INSERT INTO customers (name, email, created_at) VALUES
('Aarav Sharma', 'aarav.sharma@example.in', '2024-01-15'),
('Priya Iyer', 'priya.iyer@example.in', '2024-02-10'),
('Rohan Mehta', 'rohan.mehta@example.in', '2024-03-05'),
('Neha Reddy', 'neha.reddy@example.in', '2024-03-20'),
('Vikram Singh', 'vikram.singh@example.in', '2024-04-12'),
('Kavya Nair', 'kavya.nair@example.in', '2024-05-01'),
('Aditya Joshi', 'aditya.joshi@example.in', '2024-05-15'),
('Ishita Desai', 'ishita.desai@example.in', '2024-06-02'),
('Manish Agarwal', 'manish.agarwal@example.in', '2024-06-15'),
('Pooja Bhatia', 'pooja.bhatia@example.in', '2024-07-01'),
('Harshita Sinha', 'harshita.sinha@example.in', '2024-07-10'),
('Karan Verma', 'karan.verma@example.in', '2024-07-15'),
('Simran Kaur', 'simran.kaur@example.in', '2024-07-20'),
('Ankit Pandey', 'ankit.pandey@example.in', '2024-07-25'),
('Sneha Patil', 'sneha.patil@example.in', '2024-07-30');



INSERT INTO products (name, category, price) VALUES
('Tata Tea Gold', 'Beverages', 120.00),
('Aashirvaad Atta 5kg', 'Grocery', 280.00),
('Parle-G Biscuits', 'Snacks', 10.00),
('Dabur Honey 250g', 'Health', 199.00),
('Himalaya Face Wash', 'Personal Care', 150.00),
('Fortune Sunflower Oil 1L', 'Grocery', 140.00),
('Dettol Handwash', 'Household', 99.00),
('Amul Butter 500g', 'Dairy', 245.00),
('Samsung Galaxy M14', 'Electronics', 13999.00),
('Boat Rockerz 255', 'Electronics', 1299.00),
('Maggi 12-pack', 'Snacks', 96.00),
('Colgate Toothpaste 200g', 'Personal Care', 89.00),
('Lijjat Papad', 'Snacks', 85.00),
('Prestige Induction Cooker', 'Kitchen Appliances', 3499.00),
('Surf Excel 1kg', 'Household', 195.00);



INSERT INTO orders (customer_id, order_date, total_amount) VALUES
(1, '2024-04-15', 430.00),
(2, '2024-04-18', 389.00),
(3, '2024-04-20', 14299.00),
(4, '2024-04-25', 395.00),
(5, '2024-04-30', 154.00),
(6, '2024-05-03', 699.00),
(7, '2024-05-10', 138.00),
(8, '2024-06-06', 269.00),
(9, '2024-06-16', 344.00),
(10, '2024-06-25', 17000.00),
(11, '2024-07-03', 495.00),
(12, '2024-07-10', 102.00),
(13, '2024-07-18', 380.00),
(14, '2024-07-26', 1200.00),
(15, '2024-07-31', 550.00);


INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
-- Order 1
(1, 1, 2, 240.00),
(1, 3, 5, 50.00),
(1, 5, 1, 150.00),

-- Order 2
(2, 2, 1, 280.00),
(2, 7, 1, 99.00),

-- Order 3
(3, 9, 1, 13999.00),
(3, 10, 1, 1299.00),

-- Order 4
(4, 4, 1, 199.00),
(4, 8, 1, 245.00),

-- Order 5
(5, 6, 1, 140.00),
(5, 3, 1, 10.00),
(5, 7, 1, 99.00),

-- Order 6
(6, 11, 2, 192.00),
(6, 13, 1, 85.00),
(6, 5, 1, 150.00),
(6, 7, 1, 99.00),

-- Order 7
(7, 3, 10, 100.00),
(7, 12, 1, 89.00),

-- Order 8
(8, 2, 1, 280.00),
(8, 14, 1, 3499.00),

-- Order 9
(9, 6, 2, 280.00),
(9, 15, 1, 195.00),

-- Order 10
(10, 9, 1, 13999.00),
(10, 10, 2, 2598.00),
(10, 12, 1, 89.00),
(10, 5, 1, 150.00),

-- Order 11
(11, 1, 1, 120.00),
(11, 2, 1, 280.00),
(11, 7, 1, 99.00),

-- Order 12
(12, 3, 3, 30.00),
(12, 13, 1, 85.00),

-- Order 13
(13, 14, 1, 3499.00),
(13, 15, 1, 195.00),

-- Order 14
(14, 10, 1, 1299.00),
(14, 11, 1, 96.00),

-- Order 15
(15, 4, 2, 398.00),
(15, 8, 1, 245.00);
>>>>>>> a095286 (Save local changes before pull)
