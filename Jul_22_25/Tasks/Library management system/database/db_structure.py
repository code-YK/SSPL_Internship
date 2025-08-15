from database_connection import Database 

db = Database()

cursor = db.cursor

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS lms;")
cursor.execute("USE lms;")

# Create required tables: users, books, transactions
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY,
        name VARCHAR(50),
        email VARCHAR(50),
        join_date DATE
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INT PRIMARY KEY,
        title VARCHAR(50),
        author VARCHAR(50),
        total_copies INT
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INT PRIMARY KEY,
        user_id INT,
        book_id INT,
        issue_date DATE,
        due_date DATE,
        fine_amt INT,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (book_id) REFERENCES books(book_id)
    );
''')

db.commit()
db.close()

