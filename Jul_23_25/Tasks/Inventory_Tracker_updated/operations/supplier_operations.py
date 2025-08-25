from db.connection import get_connection
from tabulate import tabulate

def add_supplier(name, contact):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO supplier (name, contact) VALUES (?, ?)", (name, contact))
    conn.commit()
    conn.close()
    print("Supplier added successfully.")

def view_suppliers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT supplier_id, name, contact FROM supplier")
    rows = cursor.fetchall()
    conn.close()
    print(tabulate(rows, headers=["Supplier ID", "Name", "Contact"], tablefmt="pretty"))
