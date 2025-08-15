from database.database_connection import Database
from models.operations import LibraryOperations
from models.books import Books
from models.users import Users
from models.transactions import Transactions

def main():
    db = Database()
    ops = LibraryOperations(db)

    while True:
        print("\n--- Library Management System ---")
        print("1. Add User")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Generate Overdue Report")
        print("6. List All Books")
        print("7. List of Transactions")
        print("8. List All Users")
        print("9. Exit")
        
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            user_id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            join_date = input("Enter join date (YYYY-MM-DD): ")
            user = Users(db,user_id, name, email, join_date)
            user.add_user()
            print("User added successfully.")

        elif choice == '2':
            book_id = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            total_copies = int(input("Enter total copies: "))
            book = Books(db, book_id, title, author, total_copies)
            book.add_book()
            print("Book added successfully.")

        elif choice == '3':
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            ops.borrow_book(user_id, book_id)

        elif choice == '4':
            transaction_id = int(input("Enter transaction ID to return: "))
            ops.return_book(transaction_id)

        elif choice == '5':
            ops.over_due()

        elif choice == '6':
            Books.view_books(db)

        elif choice == '7':
            Transactions.view_transactions(db)

        elif choice == '8':
            Users.view_users(db)
        
        elif choice == '9':
            print("Exiting... Goodbye!")
            db.close()
            break
        
        else:
            print(" Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
