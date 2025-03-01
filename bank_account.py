import re
class BankAccount:
    def __init__(self, owner: str, balance: float, account_number: str):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number

class User:
    def __init__(self, first_name: str, last_name: str, phone: str, email: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone = phone
        self.__email = User.validate_email(email)

    def __str__(self):
        return f"User - First name: {self.__first_name}, Last name: {self.__last_name}, Phone: {self.__phone}, Email: {self.__email}"

    @staticmethod
    def validate_email(email: str):
        pattern = r"^[a-zA-z0-9]+@[a-zA-z0-9.-]+\.[a-zA-z]{2,}$"
        if not re.match(pattern, email):
            raise ValueError("Invalid Email Address")
        else:
            return email   

    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name
    
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

