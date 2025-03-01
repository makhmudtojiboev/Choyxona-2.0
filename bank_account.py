import re
class BankAccount:
    def __init__(self, owner: str, balance: float, account_number: str):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number

class User:
    def __init__(self, full_name: str, phone: str, email: str):
        self.__full_name = full_name
        self.__phone = phone
        self.__email = User.validate_email(email)

    def __str__(self):
        return f"User - Full name: {self.__full_name}, Phone: {self.__phone}, Email: {self.__email}"

    @staticmethod
    def validate_email(email: str):
        pattern = r"^[a-zA-z0-9]+@[a-zA-z0-9.-]+\.[a-zA-z]{2,}$"
        if not re.match(pattern, email):
            raise ValueError("Invalid Email Address")
        else:
            return email   

    @property
    def full_name(self):
        return self.__full_name
    
    @full_name.setter
    def full_name(self, full_name):
        self.__full_name = full_name
    
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone):
        self.__phone = phone 
    
    @property 
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email

