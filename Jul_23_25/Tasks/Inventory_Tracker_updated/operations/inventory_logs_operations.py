from db.connection import get_connection
from tabulate import tabulate

def view_logs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT l.log_id, p.name, w.name, l.txn_type, l.quantity, l.txn_date, l.total_amount
        FROM inventory_log l
        JOIN product p ON l.product_id = p.product_id
        JOIN warehouse w ON l.warehouse_id = w.warehouse_id
    """)
    rows = cursor.fetchall()
    conn.close()
    print(tabulate(rows, 
                   headers=["Log ID", "Product", "Warehouse", "Txn Type", "Qty", "Date", "Total"], 
                   tablefmt="pretty"))
