from .connection import get_connection
from datetime import datetime

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert sample products
    products = [
        ("Parle-G Biscuits", 10.0, "Snacks"),
        ("Amul Milk 1L", 60.0, "Dairy"),
        ("Tata Salt 1kg", 25.0, "Grocery"),
        ("Surf Excel 1kg", 180.0, "Detergent"),
        ("Maggi Noodles", 15.0, "Snacks"),
        ("Fortune Oil 1L", 150.0, "Grocery"),
        ("Red Label Tea 500g", 250.0, "Beverages"),
        ("Godrej Hair Dye", 90.0, "Personal Care"),
        ("Colgate Toothpaste 200g", 120.0, "Personal Care"),
        ("Pepsi 2L Bottle", 95.0, "Beverages"),
    ]
    cursor.executemany("INSERT INTO product (name, price, category) VALUES (?, ?, ?)", products)

    # Insert sample suppliers
    suppliers = [
        ("Hindustan Unilever", "022-33445566"),
        ("ITC Limited", "033-22882233"),
        ("Amul Dairy", "079-12345678"),
        ("Nestle India", "011-44447777"),
        ("PepsiCo India", "0124-2223334"),
    ]
    cursor.executemany("INSERT INTO supplier (name, contact) VALUES (?, ?)", suppliers)

    # Insert sample warehouses
    warehouses = [
        ("Mumbai Central Warehouse", "Mumbai"),
        ("Delhi NCR Warehouse", "Delhi"),
        ("Bangalore Distribution Hub", "Bangalore"),
        ("Kolkata Main Storage", "Kolkata"),
        ("Ahmedabad Regional Depot", "Ahmedabad"),
    ]
    cursor.executemany("INSERT INTO warehouse (name, location) VALUES (?, ?)", warehouses)

    # Insert some initial inventory
    inventory = [
        (1, 1, 500),   # Parle-G in Mumbai
        (2, 1, 200),   # Amul Milk in Mumbai
        (3, 2, 1000),  # Tata Salt in Delhi
        (4, 3, 300),   # Surf Excel in Bangalore
        (5, 2, 700),   # Maggi in Delhi
        (6, 4, 400),   # Fortune Oil in Kolkata
        (7, 5, 150),   # Red Label Tea in Ahmedabad
    ]
    cursor.executemany("INSERT INTO inventory (product_id, warehouse_id, quantity) VALUES (?, ?, ?)", inventory)

    # Insert sample inventory logs
    logs = [
        (1, 1, "purchase", 500, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 500 * 10),
        (2, 1, "purchase", 200, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 200 * 60),
        (3, 2, "purchase", 1000, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 1000 * 25),
        (4, 3, "purchase", 300, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 300 * 180),
        (5, 2, "purchase", 700, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 700 * 15),
        (6, 4, "purchase", 400, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 400 * 150),
        (7, 5, "purchase", 150, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 150 * 250),
        (1, 1, "sale", 50, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 50 * 10),
        (5, 2, "sale", 100, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 100 * 15),
    ]
    cursor.executemany("""
        INSERT INTO inventory_log (product_id, warehouse_id, txn_type, quantity, txn_date, total_amount) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, logs)

    conn.commit()
    conn.close()
    print("Seed data inserted successfully.")

if __name__ == "__main__":
    seed_data()
