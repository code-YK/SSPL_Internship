from db.connection import get_connection
from tabulate import tabulate

def add_warehouse(name, location):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO warehouse (name, location) VALUES (?, ?)", (name, location))
    conn.commit()
    conn.close()
    print("Warehouse added successfully.")

def view_warehouses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT warehouse_id, name, location FROM warehouse")
    rows = cursor.fetchall()
    conn.close()
    print(tabulate(rows, headers=["Warehouse ID", "Name", "Location"], tablefmt="pretty"))
