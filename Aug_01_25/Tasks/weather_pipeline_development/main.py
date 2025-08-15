from database.session import init_db
from cli import cli_menu

if __name__ == "__main__":
    init_db()
    cli_menu()