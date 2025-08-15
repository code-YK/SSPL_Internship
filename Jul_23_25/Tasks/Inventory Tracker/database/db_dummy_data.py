from db_connection import Database 

db = Database()

cursor = db.cursor

cursor.execute('USE inventory_tracker;')

cursor.executemany('''
    INSERT INTO suppliers (name, phone) VALUES (%s, %s)
''', [
    ('Ramesh Electronics', '9876543210'),
    ('Kiran Distributors', '9823456789'),
    ('Mehta Traders', '9898989898')
])


cursor.executemany('''
    INSERT INTO products (name, description, supplier_id) VALUES (%s, %s, %s)
''', [
    ('LED Bulb 9W', 'Energy efficient LED bulb', 1),
    ('Bluetooth Speaker', 'Portable speaker with mic', 2),
    ('Laptop Backpack', 'Waterproof 15.6 inch bag', 3),
    ('USB Keyboard', 'Standard wired keyboard', 1)
])



cursor.executemany('''
    INSERT INTO warehouses (name, location) VALUES (%s, %s)
''', [
    ('Mumbai Warehouse', 'Andheri East, Mumbai'),
    ('Delhi Warehouse', 'Okhla Phase 2, Delhi'),
    ('Bangalore Warehouse', 'Whitefield, Bangalore')
])




cursor.executemany('''
    INSERT INTO inventory_logs (product_id, warehouse_id, quantity, change_type, notes)
    VALUES (%s, %s, %s, %s, %s)
''', [
    # Stock IN
    (1, 1, 100, 'IN', 'First stock for LED Bulbs'),
    (2, 1, 50, 'IN', 'Bluetooth speakers delivery'),
    (3, 2, 75, 'IN', 'New bags received'),
    (4, 3, 60, 'IN', 'Keyboards delivered'),

    # Stock OUT
    (1, 1, 15, 'OUT', 'Retail sale: LED Bulbs'),
    (2, 1, 10, 'OUT', 'Online order shipped'),
    (3, 2, 20, 'OUT', 'Dispatched to client'),
    (4, 3, 5,  'OUT', 'Damaged unit removed')
])


db.commit()
cursor.close()
db.close()
