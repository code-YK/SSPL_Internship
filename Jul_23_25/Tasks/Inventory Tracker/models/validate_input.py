class Validate_Input:
    
    def __init__(self):
        pass

    # to validate int inputs
    def check_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # to validate non-empty and string inputs 
    def check_nonempty_input(self, prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty. Please try again.")

    # to validate phone number format
    def check_valid_phone(self, prompt):
        while True:
            phone = input(prompt).strip()
            if phone.isdigit() and len(phone) == 10:
                return phone
            print("Invalid phone number. Enter exactly 10 digits.")
