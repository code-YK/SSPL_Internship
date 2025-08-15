from database.db_connection import Database

db = Database()

class Warehouses:
    def __init__(self, db, name, location):
        self.db = db
        self.name = name
        self.location = location

    def add_warehouse(self):
        query = "INSERT INTO warehouses (name, location) VALUES (%s, %s)"
        self.db.cursor.execute(query, (self.name, self.location))
        self.db.commit()
        print("Warehouse added!")

    @staticmethod
    def view_warehouses(db):
        db.cursor.execute("SELECT * FROM warehouses")
        warehouses = db.cursor.fetchall()
        print('--'*4 + 'WAREHOUSES' + '--'*4)
        print('warehouse_id, name, location')
        for warehouse in warehouses:
            print(warehouse)