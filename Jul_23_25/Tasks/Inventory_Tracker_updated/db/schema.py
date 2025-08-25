from .connection import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS supplier (
            supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS warehouse (
            warehouse_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            warehouse_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY(product_id) REFERENCES product(product_id),
            FOREIGN KEY(warehouse_id) REFERENCES warehouse(warehouse_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory_log (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            warehouse_id INTEGER,
            txn_type TEXT,
            quantity INTEGER,
            txn_date TEXT,
            total_amount REAL,
            FOREIGN KEY(product_id) REFERENCES product(product_id),
            FOREIGN KEY(warehouse_id) REFERENCES warehouse(warehouse_id)
        )
    """)

    conn.commit()
    conn.close()
