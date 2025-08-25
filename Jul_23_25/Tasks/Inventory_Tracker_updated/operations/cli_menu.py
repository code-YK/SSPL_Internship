from operations.product_operations import add_product, view_products
from operations.supplier_operations import add_supplier, view_suppliers
from operations.warehouse_operations import add_warehouse, view_warehouses
from operations.inventory_operations import add_stock, remove_stock, view_inventory
from operations.inventory_logs_operations import view_logs

def menu():
    while True:
        print("\n=== Inventory Tracker CLI ===")
        print("1. Add Product")
        print("2. View Products")
        print("3. Add Supplier")
        print("4. View Suppliers")
        print("5. Add Warehouse")
        print("6. View Warehouses")
        print("7. Add Stock")
        print("8. Remove Stock")
        print("9. View Inventory")
        print("10. View Logs")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Product Name: ")
            price = float(input("Price: "))
            category = input("Category: ")
            add_product(name, price, category)
        elif choice == "2":
            view_products()
        elif choice == "3":
            name = input("Supplier Name: ")
            contact = input("Contact: ")
            add_supplier(name, contact)
        elif choice == "4":
            view_suppliers()
        elif choice == "5":
            name = input("Warehouse Name: ")
            location = input("Location: ")
            add_warehouse(name, location)
        elif choice == "6":
            view_warehouses()
        elif choice == "7":
            pid = int(input("Product ID: "))
            wid = int(input("Warehouse ID: "))
            qty = int(input("Quantity: "))
            add_stock(pid, wid, qty)
        elif choice == "8":
            pid = int(input("Product ID: "))
            wid = int(input("Warehouse ID: "))
            qty = int(input("Quantity: "))
            remove_stock(pid, wid, qty)
        elif choice == "9":
            view_inventory()
        elif choice == "10":
            view_logs()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")
