from database.db_connection import Database
from models.products import Products
from models.suppliers import Suppliers
from models.warehouses import Warehouses
from models.inventory_logs import InventoryLogs
from models.operations import Operations
from models.validate_input import Validate_Input

def main():
    print("\nInventory Management System")
    db = Database()
    ops = Operations(db)
    validator = Validate_Input()

    while True:
        print("\n" + "--" * 20)
        print("\nMenu:")
        print("1. Add Product")
        print("2. View Products")
        print("3. Add Supplier")
        print("4. View Suppliers")
        print("5. Add Warehouse")
        print("6. View Warehouses")
        print("7. Add Inventory Log")
        print("8. View Incoming Orders")
        print("9. View Outgoing Orders")
        print("10. Exit")
        print("\n" + "--" * 20)

        choice = input("Enter your choice: ")
        if choice == '1':
            name = validator.check_nonempty_input("Enter product name: ")
            description = validator.check_nonempty_input("Enter product description: ")
            supplier_id = validator.check_int_input("Enter supplier ID: ")
            product = Products(db, name, description, supplier_id)
            product.add_product()

        elif choice == '2':
            Products.view_products(db)

        elif choice == '3':
            name = validator.check_nonempty_input("Enter supplier name: ")
            phone = validator.check_valid_phone("Enter supplier phone (10 digits): ")
            supplier = Suppliers(db, name, phone)
            supplier.add_supplier()

        elif choice == '4':
            Suppliers.view_suppliers(db)
        
        elif choice == '5':
            name = validator.check_nonempty_input("Enter warehouse name: ")
            location = validator.check_nonempty_input("Enter warehouse location: ")
            warehouse = Warehouses(db, name, location)
            warehouse.add_warehouse()

        elif choice == '6':
            Warehouses.view_warehouses(db)

        elif choice == '7':
            product_id = validator.check_int_input("Enter product ID: ")
            warehouse_id = validator.check_int_input("Enter warehouse ID: ")
            quantity = validator.check_int_input("Enter quantity: ")
            change_type = validator.check_nonempty_input("Enter change type (IN/OUT): ").strip().upper()
            notes = validator.check_nonempty_input("Enter notes: ")
            log = InventoryLogs(db, product_id, warehouse_id, quantity, change_type, notes)
            log.add_inventory_log()

        elif choice == '8':
            ops.view_incoming_orders()
        
        elif choice == '9':
            ops.view_outgoing_orders()

        elif choice == '10':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")  

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)