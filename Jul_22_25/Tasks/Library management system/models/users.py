from database.database_connection import Database

db = Database()

class Users:
    def __init__(self,db,user_id,name,email,join_date):
        self.db=db
        self.user_id=user_id
        self.name=name
        self.email=email
        self.join_date=join_date

    def add_user(self):
        query = "INSERT INTO users (user_id,name,email,join_date) VALUES (%s, %s, %s, %s);"
        self.db.cursor.execute(query,(self.user_id,self.name,self.email,self.join_date))
        self.db.commit()
        print("User added!")
    
    @staticmethod
    def view_users(db):
        db.cursor.execute("SELECT * FROM users")
        users = db.cursor.fetchall()
        print('--'*4 + 'USERS'+ '--'*4)
        for user in users:
            print(user)