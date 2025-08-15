from database.setup import Database
from models.users import User
from models.books import Book
from models.transactions import Transaction


db = Database()
session = db.get_session()


def dummy_users():
    users = [
        User(name="Rohan Sharma", email="rohan.sharma@gmail.com", join_date="2024-01-10"),
        User(name="Anjali Mehta", email="anjali.mehta@gmail.com", join_date="2024-02-12"),
        User(name="Karan Patel", email="karan.patel@gmail.com", join_date="2024-03-05"),
        User(name="Priya Deshmukh", email="priya.deshmukh@gmail.com", join_date="2024-04-18"),
        User(name="Nikhil Verma", email="nikhil.verma@gmail.com", join_date="2024-05-22"),
    ]
    session.add_all(users)
    session.commit()

    
def dummy_books():
    books = [
        Book(title="Wings of Fire", author="A.P.J. Abdul Kalam", total_copies=5, available_copies=3),
        Book(title="The White Tiger", author="Aravind Adiga", total_copies=4, available_copies=2),
        Book(title="Train to Pakistan", author="Khushwant Singh", total_copies=6, available_copies=4),
        Book(title="The Guide", author="R. K. Narayan", total_copies=3, available_copies=1),
        Book(title="Ignited Minds", author="A.P.J. Abdul Kalam", total_copies=7, available_copies=6),
    ]
    session.add_all(books)
    session.commit()

def dummy_transactions():
    transactions = [
        Transaction(user_id=1, book_id=1, issue_date="2024-07-01", return_date="2024-07-10", fine_amount=0),
        Transaction(user_id=2, book_id=2, issue_date="2024-07-05", return_date=None, fine_amount=None),
        Transaction(user_id=3, book_id=3, issue_date="2024-07-10", return_date="2024-07-17", fine_amount=0),
        Transaction(user_id=1, book_id=5, issue_date="2024-07-18", return_date=None, fine_amount=None),
        Transaction(user_id=4, book_id=4, issue_date="2024-07-20", return_date="2024-07-29", fine_amount=10),
    ]
    session.add_all(transactions)
    session.commit()

def insert_all():
    try:
        dummy_users()
        dummy_books()
        dummy_transactions()
        print("Seeded all data successfully.")
    except Exception as e:
        session.rollback()
        print("Seeding failed:", e)
    finally:
        session.close()

if __name__ == "__main__":
    insert_all()
