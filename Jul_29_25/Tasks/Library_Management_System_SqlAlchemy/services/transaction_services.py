from database.setup import Database
from models.transactions import Transaction
from models.books import Book
from models.users import User
from datetime import datetime, timedelta
from tabulate import tabulate

db = Database()

class TransactionService:
    def __init__(self):
        self.db = db

    def borrow_book(self, user_id, book_id):
        session = self.db.get_session()
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            book = session.query(Book).filter(Book.book_id == book_id).first()
            if not user or not book:
                print("User or Book not found.")
                return
            if book.available_copies <= 0:
                print("No available copies of the book.")
                return

            transaction = Transaction(
                user_id=user.user_id,
                book_id=book.book_id,
                issue_date=datetime.today().date().strftime("%Y-%m-%d")
            )
            book.available_copies -= 1
            session.add(transaction)
            session.commit()
            print("Book borrowed successfully.")
        except Exception as e:
            session.rollback()
            print("Failed to borrow book:", e)
        finally:
            session.close()

    def return_book(self, user_id, book_id):
        session = self.db.get_session()
        try:
            transaction = session.query(Transaction).filter(
                Transaction.user_id == user_id,
                Transaction.book_id == book_id,
                Transaction.return_date == None
            ).first()
            if not transaction:
                print("No active transaction found for this book.")
                return

            # Ensure issue_date is a date
            issue_date = transaction.issue_date
            if isinstance(issue_date, str):
                issue_date = datetime.strptime(issue_date, "%Y-%m-%d").date()
            elif isinstance(issue_date, datetime):
                issue_date = issue_date.date()

            # Make today a date object
            today = datetime.today().date()
            due_date = issue_date + timedelta(days=7)

            if today > due_date:
                days_overdue = (today - due_date).days
                transaction.fine_amount = days_overdue * 10
                print(f"Fine incurred: ₹{transaction.fine_amount}")
            else:
                transaction.fine_amount = 0

            transaction.return_date = today.strftime("%Y-%m-%d")
            book = session.query(Book).filter(Book.book_id == book_id).first()
            book.available_copies += 1

            session.commit()
            print("Book returned successfully.")
        except Exception as e:
            session.rollback()
            print("Failed to return book:", e)
        finally:
            session.close()

    def over_due_books(self):
        session = self.db.get_session()
        try:
            transactions = session.query(Transaction).filter(
                Transaction.return_date == None
            ).all()

            overdue_transactions = []
            today = datetime.today().date()

            for t in transactions:
                issue_date = t.issue_date
                if isinstance(issue_date, str):
                    issue_date = datetime.strptime(issue_date, "%Y-%m-%d").date()

                due_date = issue_date + timedelta(days=7)

                if today > due_date:
                    days_overdue = (today - due_date).days
                    t.fine_amount = days_overdue * 10
                    overdue_transactions.append(t)

            if not overdue_transactions:
                print("No overdue books found.")
                return

            session.commit()

            table_data = [[
                t.transaction_id,
                t.user_id,
                t.book_id,
                t.issue_date,
                t.return_date if t.return_date else "Not Returned",
                t.fine_amount
            ] for t in overdue_transactions]

            print("--" * 4 + " Overdue Transactions " + "--" * 4)
            print(tabulate(table_data, headers=[
                "Transaction ID", "User ID", "Book ID", "Issue Date", "Return Date", "Fine Amount"
            ], tablefmt="fancy_grid"))

        except Exception as e:
            print("Failed to retrieve overdue books:", e)
        finally:
            session.close()

    def view_transactions(self):
        session = self.db.get_session()
        try:
            transactions = session.query(Transaction).all()
            if not transactions:
                print("No transactions found.")
                return

            table_data = [[
                t.transaction_id,
                t.user_id,
                t.book_id,
                t.issue_date,
                t.return_date if t.return_date else "Not Returned",
                t.fine_amount
            ] for t in transactions]

            print("--" * 4 + " All Transactions " + "--" * 4)
            print(tabulate(table_data, headers=[
                "Transaction ID", "User ID", "Book ID", "Issue Date", "Return Date", "Fine Amount"
            ], tablefmt="fancy_grid"))

        except Exception as e:
            print("Failed to retrieve transactions:", e)
        finally:
            session.close()
