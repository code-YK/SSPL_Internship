from database.db_connection import Database

db = Database()

class Operations:
    def __init__(self,db):
        self.db = db


    def view_incoming_orders(self):
        query = ''' 
            SELECT 
                i.log_id,
                i.product_id,
                p.name AS product_name,
                s.name AS supplier_name,
                w.name AS warehouse_name,
                i.quantity,
                i.change_type
            FROM 
                inventory_logs AS i
            JOIN
                products AS p ON i.product_id = p.product_id
            JOIN
                suppliers AS s ON p.supplier_id = s.supplier_id
            JOIN
                warehouses AS w ON i.warehouse_id = w.warehouse_id
            WHERE
                i.change_type = 'IN';
            ''' 
        self.db.cursor.execute(query)
        orders = self.db.cursor.fetchall() 
        print('--'*4 + 'INCOMING ORDERS' + '--'*4)
        print('log_id, product_id, product_name, supplier_name, warehouse_name, quantity, change_type')
        for order in orders:
            print(order)


    def view_outgoing_orders(self):
        query = ''' 
            SELECT 
                i.log_id,
                i.product_id,
                p.name AS product_name,
                s.name AS buyer_name,
                w.name AS warehouse_name,
                i.quantity,
                i.change_type
            FROM 
                inventory_logs AS i
            JOIN
                products AS p ON i.product_id = p.product_id
            JOIN
                suppliers AS s ON p.supplier_id = s.supplier_id
            JOIN
                warehouses AS w ON i.warehouse_id = w.warehouse_id
            WHERE
                i.change_type = 'OUT';
            ''' 
        self.db.cursor.execute(query)
        orders = self.db.cursor.fetchall() 
        print('--'*4 + 'OUTGOING ORDERS' + '--'*4)
        print('log_id, product_id, product_name, buyer_name, warehouse_name, quantity, change_type')
        for order in orders:
            print(order)