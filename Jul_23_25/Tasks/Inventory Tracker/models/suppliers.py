from database.db_connection import Database

db = Database()

class Suppliers:
    def __init__(self, db, name, phone):
        self.db = db
        self.name = name
        self.phone = phone

    def add_supplier(self):
        query = "INSERT INTO suppliers (name, phone) VALUES (%s, %s)"
        self.db.cursor.execute(query, (self.name, self.phone))
        self.db.commit()
        print("Supplier added!")

    @staticmethod
    def view_suppliers(db):
        db.cursor.execute("SELECT * FROM suppliers")
        suppliers = db.cursor.fetchall()
        print('--'*4 + 'SUPPLIERS' + '--'*4)
        print('supplier_id, name, phone')
        for supplier in suppliers:
            print(supplier)