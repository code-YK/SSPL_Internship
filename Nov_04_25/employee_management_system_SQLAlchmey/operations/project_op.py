from datetime import date
from sqlalchemy.exc import SQLAlchemyError
from models import Project

# add a new project
def add_project(session, name: str, start_date: date, end_date: date = None):
    try:
        new_project = Project(name=name, start_date=start_date, end_date=end_date)
        session.add(new_project)
        session.commit()
        print(f"Added project: {new_project.name} with ID {new_project.project_id}")
    except SQLAlchemyError as e:
        session.rollback()
        raise e

# View all projects
def view_all_projects(session):
    try:
        projects = session.query(Project).all()
        for proj in projects:
            print(f"""
                  ID: {proj.project_id}, 
                  Name: {proj.name}, 
                  Start Date: {proj.start_date}, 
                  End Date: {proj.end_date}
                -------------------------------""")
    except SQLAlchemyError as e:
        raise e
    

# view all ongoing projects
def view_ongoing_projects(session):
    try:
        today = date.today()
        ongoing_projects = session.query(Project).filter(
            (Project.end_date == None) | (Project.end_date >= today)
        ).all()
        for proj in ongoing_projects:
            print(f"""
                  ID: {proj.project_id}, 
                  Name: {proj.name}, 
                  Start Date: {proj.start_date}, 
                  End Date: {proj.end_date}
                -------------------------------""")
    except SQLAlchemyError as e:
        raise e