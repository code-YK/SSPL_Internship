from database.database_connection import Database
from datetime import date, timedelta

db = Database()

class LibraryOperations:
    
    def __init__(self, db):
        self.db = db



    def borrow_book(self, user_id, book_id):
        # Generate new transaction ID
        self.db.cursor.execute("SELECT MAX(transaction_id) FROM transactions")
        last_id = self.db.cursor.fetchone()[0]
        new_id = 1 if last_id is None else last_id + 1

        # Set dates
        issue_date = date.today()
        due_date = issue_date + timedelta(days=7)

        # Insert transaction (fine_amt initially 0)
        query="""
        INSERT INTO transactions 
        (transaction_id, user_id, book_id, issue_date, due_date, fine_amt) 
        VALUES (%s, %s, %s, %s, %s, %s);"""

        self.db.cursor.execute(query,(new_id, user_id, book_id, issue_date, due_date, 0))

        self.db.commit()
        print(f"Book borrowed successfully! Transaction ID: {new_id}")




    def return_book(self,transaction_id):

        #checking if book is overdue or not
        today=date.today()
        query = "SELECT due_date FROM transactions WHERE transaction_id = %s;"
        self.db.cursor.execute(query, (transaction_id))
        due = self.db.cursor.fetchone()[0]

        if due < today:
            days_late = (today - due).days
            fine = days_late * 10
            print(f"The book is overdue. Please pay Rs.{fine}")

            # Update fine_amt in database
            update_query = "UPDATE transactions SET fine_amt = %s WHERE transaction_id = %s;"
            self.db.cursor.execute(update_query, (fine, transaction_id))
            self.db.commit()

        else:
            print("Book returned successfully!!")



    def over_due(self):
        
        today=date.today()
        query = '''SELECT 
                    t.transaction_id,
                    u.name,
                    b.title,
                    t.issue_date,
                    t.due_date 
                   FROM transactions as t
                   JOIN users as u ON t.user_id=u.user_id
                   JOIN books as b ON t.book_id=b.book_id;'''
        self.db.cursor.execute(query)
        
        dues = self.db.cursor.fetchall()
        
        print('--'*4 + 'Over_Due Report' + '--'*4)
        for due in dues:
            if due[4] < today:
                print(due)
