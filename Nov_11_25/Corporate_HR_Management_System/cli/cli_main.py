from .cli_department import department_menu
from .cli_employee import employee_menu
from .cli_payroll import payroll_menu
from .cli_leaveRecord import leaveRecord_menu

def main_menu():
    while True:
        print("====Corporate HR Management System Main Menu:====")
        print("1. Department Management")
        print("2. Employee Management")
        print("3. Payroll Management")
        print("4. Leave Record Management")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            department_menu()
        elif choice == '2':
            employee_menu()
        elif choice == '3':
            payroll_menu()
        elif choice == '4':
            leaveRecord_menu()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")