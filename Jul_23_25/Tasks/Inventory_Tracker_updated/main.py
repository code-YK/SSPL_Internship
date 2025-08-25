from db.schema import create_tables
from operations.cli_menu import menu

if __name__ == "__main__":
    # Create all tables before starting
    create_tables()

    # Launch CLI menu
    menu()
