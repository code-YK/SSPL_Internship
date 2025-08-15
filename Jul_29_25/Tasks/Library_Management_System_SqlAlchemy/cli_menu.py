class Menu:
    def __init__(self):
        pass

    def display_menu(self):
        print("\n"+"--"*4 + "Library Management System Menu:" + "--"*4)
        print("1. Add User")
        print("2. Update User")
        print("3. View Users")
        print("4. Add Book")
        print("5. Update Book")
        print("6. View Books")
        print("7. Delete Book")
        print("8. Delete User")
        print("9. Borrow Book")
        print("10. Return Book")
        print("11. View Overdue Books")
        print("12. View Transactions")
        print("13. Exit")
        print("--"*12)
    
    def get_choice(self):
        choice = input("Enter your choice: ")
        return choice.strip()