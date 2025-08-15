from database.setup import Database
from models.users import User
from tabulate import tabulate
from datetime import date

db = Database()

class UserService:
    def __init__(self):
        self.db = db


    def add_user(self, name, email):
        session = self.db.get_session()
        try:
            user = User(name=name, email=email ,join_date=date.today())
            session.add(user)
            session.commit()
            print("User added successfully.")
        except Exception as e:
            session.rollback()
            print("Failed:", e)
        finally:
            session.close()


    def update_user(self, user_id, name=None, email=None):
        session = self.db.get_session()
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            if not user:
                print("User not found.")
                return
            if name:
                user.name = name
            if email:
                user.email = email
            session.commit()
            print("User updated successfully.")
        except Exception as e:
            session.rollback()
            print("Failed to update user:", e)
        finally:
            session.close()


    def view_users(self):
        session = self.db.get_session()
        try:
            users = session.query(User).all()
            table_data = [[user.user_id, user.name, user.email] for user in users]
            if not table_data:
                print("No users found.")
                return
            print('--'*4 + "All Users" + '--'*4)
            print(tabulate(table_data, headers=["User ID", "Name", "Email"], tablefmt="fancy_grid"))
        except Exception as e:
            print("Failed to retrieve users:", e)
        finally:
            session.close()


    def delete_user(self, user_id):
        session = self.db.get_session()
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            if user:
                session.delete(user)
                session.commit()
                print("User deleted successfully.")
            else:
                print("User not found.")
        except Exception as e:
            session.rollback()
            print("Failed to delete user:", e)
        finally:
            session.close()