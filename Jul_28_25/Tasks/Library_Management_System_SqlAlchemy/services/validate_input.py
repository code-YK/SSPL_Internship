from datetime import datetime


class Validate_Input:
    def __init__(self):
        pass

    def check_int_input(self, input_value):
        try:
            if type(input_value) is not int:
                value = int(input_value)
            else:
                value = input_value
            return value
        except ValueError:
            raise ValueError("Invalid input: Please enter a valid integer.")
        

    def check_str_input(self, input_value):
        try:
            if type(input_value) is not str:
                print("Invalid Input : Please enter a valid string.")
            else:
                value = input_value
            return value.strip()
        except ValueError:
            raise ValueError("Invalid input: Please enter a valid string.")
        
    
    def check_date_fmt(self, input_value):
        try:
            date_obj = datetime.strptime(str(input_value), "%Y-%m-%d")
            return date_obj.date()
        except ValueError:
            raise ValueError("Invalid input: Please enter date in YYYY-MM-DD format.")