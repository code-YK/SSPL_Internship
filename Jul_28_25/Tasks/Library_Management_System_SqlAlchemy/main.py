from database.setup import Database
from services.book_services import BookService
from services.user_services import UserService
from services.transaction_services import TransactionService
from services.validate_input import Validate_Input

def display_menu():
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


def get_choice():
    choice = int(input("Enter your choice: "))
    return choice


def main():
    db = Database()
    db.create_tables()
    book_service = BookService()
    user_service = UserService()
    transaction_service = TransactionService()
    is_valid = Validate_Input()
    
    while True:
        display_menu()
        choice = get_choice()
        if choice == 1:
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            user_service.add_user(name, email)

        elif choice == 2:
            user_id = int(input("Enter user ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            user_service.update_user(user_id, name or None, email or None)

        elif choice == 3:
            user_service.view_users()

        elif choice == 4:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            total_copies = int(input("Enter total copies: "))
            available_copies = input("Enter available copies (leave blank for total): ")
            book_service.add_book(title, author, total_copies, int(available_copies) if available_copies else None)    

        elif choice == 5:
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter new title (leave blank to keep current): ")
            author = input("Enter new author (leave blank to keep current): ")
            total_copies = input("Enter new total copies (leave blank to keep current): ")
            available_copies = input("Enter new available copies (leave blank to keep current): ")
            book_service.update_book(
                book_id, 
                title or None, 
                author or None, 
                int(total_copies) if total_copies else None, 
                int(available_copies) if available_copies else None
            )
        
        elif choice == 6:
            book_service.view_books()

        elif choice == 7:
            book_id = int(input("Enter book ID to delete: "))
            book_service.delete_book(book_id)

        elif choice == 8:
            user_id = int(input("Enter user ID to delete: "))
            user_service.delete_user(user_id)
        
        elif choice == 9:
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            transaction_service.borrow_book(user_id, book_id)

        elif choice == 10:
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            transaction_service.return_book(user_id, book_id)

        elif choice == 11:
            transaction_service.over_due_books()

        elif choice == 12:
            transaction_service.view_transactions()
        
        elif choice == 13:
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()  