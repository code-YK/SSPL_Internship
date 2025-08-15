from db_connection import Database 

db = Database()

cursor = db.cursor

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS Inventory_Tracker;")
cursor.execute("USE Inventory_Tracker;")

# Create required tables: suppliers,products,warehouses,inventory_logs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS suppliers (
        supplier_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20)
);
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        description TEXT,
        supplier_id INT,
        FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS warehouses (
        warehouse_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        location VARCHAR(100) NOT NULL
);
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory_logs (
        log_id INT AUTO_INCREMENT PRIMARY KEY,
        product_id INT,
        warehouse_id INT,
        quantity INT NOT NULL,
        change_type ENUM('IN', 'OUT') NOT NULL,
        log_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        notes TEXT,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);
''')
        
db.commit()
cursor.close()
db.close()