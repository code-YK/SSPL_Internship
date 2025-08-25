from db.connection import get_connection
from tabulate import tabulate
from datetime import datetime

def add_stock(product_id, warehouse_id, quantity):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT price FROM product WHERE product_id=?", (product_id,))
    product = cursor.fetchone()
    if not product:
        print("Product not found.")
        return
    price = product[0]

    cursor.execute("""SELECT inventory_id, quantity 
                   FROM inventory 
                   WHERE product_id=? AND warehouse_id=?""", 
                   (product_id, warehouse_id))
    row = cursor.fetchone()

    if row:
        cursor.execute("UPDATE inventory SET quantity=? WHERE inventory_id=?", (row[1] + quantity, row[0]))
    else:
        cursor.execute("INSERT INTO inventory (product_id, warehouse_id, quantity) VALUES (?, ?, ?)", 
                       (product_id, warehouse_id, quantity))

    cursor.execute("""
        INSERT INTO inventory_log (product_id, warehouse_id, txn_type, quantity, txn_date, total_amount) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, (product_id, warehouse_id, "purchase", quantity, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), price * quantity))

    conn.commit()
    conn.close()
    print("Stock added successfully.")

def remove_stock(product_id, warehouse_id, quantity):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT price FROM product WHERE product_id=?", (product_id,))
    product = cursor.fetchone()
    if not product:
        print("Product not found.")
        return
    price = product[0]

    cursor.execute("SELECT inventory_id, quantity FROM inventory WHERE product_id=? AND warehouse_id=?", 
                   (product_id, warehouse_id))
    row = cursor.fetchone()

    if not row or row[1] < quantity:
        print("Not enough stock.")
        return

    cursor.execute("UPDATE inventory SET quantity=? WHERE inventory_id=?", (row[1] - quantity, row[0]))

    cursor.execute("""
        INSERT INTO inventory_log (product_id, warehouse_id, txn_type, quantity, txn_date, total_amount) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, (product_id, warehouse_id, "sale", quantity, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), price * quantity))

    conn.commit()
    conn.close()
    print("Stock removed successfully.")

def view_inventory():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT i.inventory_id, p.name, w.name, i.quantity 
        FROM inventory i
        JOIN product p ON i.product_id = p.product_id
        JOIN warehouse w ON i.warehouse_id = w.warehouse_id
    """)
    rows = cursor.fetchall()
    conn.close()
    print(tabulate(rows, headers=["Inventory ID", "Product", "Warehouse", "Quantity"], tablefmt="pretty"))
