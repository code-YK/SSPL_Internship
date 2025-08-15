from database.database_connection import Database

db = Database()

class Books:
    def __init__(self, db, book_id, title, author, total_copies):
        self.db = db
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies

    def add_book(self):
        query = "INSERT INTO books (book_id, title, author, total_copies) VALUES (%s, %s, %s, %s)"
        self.db.cursor.execute(query, (self.book_id, self.title, self.author, self.total_copies))
        self.db.commit()
        print("Book added!")

    @staticmethod
    def view_books(db):
        db.cursor.execute("SELECT * FROM books")
        print('book_id, title, author, total_copies')
        books = db.cursor.fetchall()
        print('--'*4 + 'BOOKS'+ '--'*4)
        for book in books:
            print(book)

