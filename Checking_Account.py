#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab07, exercise3, Checking Account

class Checking_Account:
    def __init__(self, cus_name, account_number, address, \
                 initial_balance):
        
        self.__cus_name = cus_name
        self.__account_number = account_number
        self.__address = address
        self.__balance = initial_balance
        self.__initial_balance = initial_balance
        self.__calculate_bal = 0
       

    def get_account_number(self):
        return self.__account_number
    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_cus_name(self):
        return self.__cus_name
    def set_cus_name(self, cus_name):
        self.__cus_name = cus_name
 
    def get_address(self):
        return self.__address
    def set_address(self, address):
        self.__address = address




        
    def debit(self, amount):
        self.__balance -= amount
    def credit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
        


    def to_string(self):
        final = self.get_balance()
       
        
        return "Customer name: " + self.__cus_name \
        + "    - Account number: " + self.__account_number \
        + "    - Customer address: " + self.__address \
        + f"    - initial: ${self.__initial_balance:.2f}" \
        + f"    - Your new balance is: ${final:.2f}" 
