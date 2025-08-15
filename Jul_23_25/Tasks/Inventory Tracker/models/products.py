from database.db_connection import Database

db = Database()

class Products:
    def __init__(self, db, name, description, supplier_id):
        self.db = db
        self.name = name
        self.description = description
        self.supplier_id = supplier_id

    def add_product(self):
        query = "INSERT INTO products (name, description, supplier_id) VALUES (%s, %s, %s)"
        self.db.cursor.execute(query, (self.name, self.description, self.supplier_id))
        self.db.commit()
        print("Product added!")

    @staticmethod
    def view_products(db):
        db.cursor.execute("SELECT * FROM products")
        products = db.cursor.fetchall()
        print('--'*4 + 'PRODUCTS' + '--'*4)
        print('product_id, name, description, supplier_id')
        for product in products:
            print(product)