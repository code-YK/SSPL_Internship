from database.db_connection import Database

db = Database()

class InventoryLogs:

    valid_change_types = ('IN','OUT')
    
    def __init__(self, db, product_id, warehouse_id, quantity, change_type, notes):
        self.db = db
        self.product_id = product_id
        self.warehouse_id = warehouse_id
        self.quantity = quantity
        self.change_type = change_type
        self.notes = notes

    def add_log(self):
        if self.change_type not in self.valid_change_types:
            raise ValueError(f"Invalid change type: {self.change_type}. Must be one of {self.valid_change_types}.")
        query = "INSERT INTO inventory_logs (product_id, warehouse_id, quantity, change_type, notes) VALUES (%s, %s, %s, %s, %s)"
        self.db.cursor.execute(query, (self.product_id, self.warehouse_id, self.quantity, self.change_type, self.notes))
        self.db.commit()
        print("Inventory log added!")

    @staticmethod
    def view_logs(db):
        db.cursor.execute("SELECT * FROM inventory_logs")
        logs = db.cursor.fetchall()
        print('--'*4 + 'INVENTORY LOGS' + '--'*4)
        print('log_id, product_id, warehouse_id, quantity, change_type, log_date, notes')
        for log in logs:
            print(log)