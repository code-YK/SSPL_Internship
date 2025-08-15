from database.database_connection import Database

db = Database()

class Transactions:
    def __init__(self,db,transaction_id,user_id,book_id,issue_date,due_date,fine_amt):
        self.db=db
        self.transaction_id=transaction_id
        self.user_id=user_id
        self.book_id=book_id
        self.issue_date=issue_date
        self.due_date=due_date
        self.fine_amt=fine_amt

    @staticmethod
    def view_transactions(db):
        query='''SELECT 
                t.transaction_id,
                t.user_id,
                u.name,
                t.book_id,
                t.fine_amt AS amount_paid
                FROM 
                transactions as t
                JOIN 
                users as u ON t.user_id = u.user_id;'''
        
        db.cursor.execute(query)
        rows=db.cursor.fetchall()
        print('--'*4 + 'TRANSACTIONS'+ '--'*4)
        for row in rows:
            print(row)