from database.setup import Database
from models.books import Book
from tabulate import tabulate

db = Database()

class BookService:
    def __init__(self):
        self.db = db


    def add_book(self, title, author, total_copies, available_copies=None):
        session = self.db.get_session()
        try:
            if available_copies is None:
                available_copies = total_copies
            book = Book(title=title, author=author, total_copies=total_copies, available_copies=available_copies)
            session.add(book)
            session.commit()
            print("Book added successfully.")
        except Exception as e:
            session.rollback()
            print("Failed to add book:", e)
        finally:
            session.close()


    def update_book(self, book_id, title=None, author=None, total_copies=None, available_copies=None):
        session = self.db.get_session()
        try:
            book = session.query(Book).filter(Book.book_id == book_id).first()
            if not book:
                print("Book not found.")
                return
            if title:
                book.title = title
            if author:
                book.author = author
            if total_copies is not None:
                book.total_copies = total_copies
            if available_copies is not None:
                book.available_copies = available_copies
            session.commit()
            print("Book updated successfully.")
        except Exception as e:
            session.rollback()
            print("Failed to update book:", e)
        finally:
            session.close()


    def view_books(self):
        session = self.db.get_session()
        try:
            books = session.query(Book).all()
            table_data = [[book.book_id, book.title, book.author, book.total_copies, book.available_copies] for book in books]
            if not table_data:
                print("No books found.")
                return
            print('--'*4 + "All Books" + '--'*4)
            print(tabulate(table_data, headers=["Book ID", "Title", "Author", "Total Copies", "Available Copies"], tablefmt="fancy_grid"))
        except Exception as e:
            print("Failed to retrieve books:", e)
        finally:
            session.close()
        

    def delete_book(self, book_id):
        session = self.db.get_session()
        try:
            book = session.query(Book).filter(Book.book_id == book_id).first()
            if book:
                session.delete(book)
                session.commit()
                print("Book deleted successfully.")
            else:
                print("Book not found.")
        except Exception as e:
            session.rollback()
            print("Failed to delete book:", e)
        finally:
            session.close()