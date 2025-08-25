from db.connection import get_connection
from tabulate import tabulate

def add_product(name, price, category):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (name, price, category) VALUES (?, ?, ?)", 
                   (name, price, category))
    conn.commit()
    conn.close()
    print("Product added successfully.")

def view_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT product_id, name, price, category FROM product")
    rows = cursor.fetchall()
    conn.close()
    print(tabulate(rows, headers=["Product ID", "Name", "Price", "Category"], tablefmt="pretty"))
