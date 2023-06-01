#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab07, exercise3, Checking account test

from Checking_Account import Checking_Account

cus_name = str(input("Enter customers name: "))
account_number = str(input("Enter account number: "))
address = str(input("Enter address: "))
initial_balance = float(input("Enter starting balance: "))
debit = float(input("Enter withdrawl amount: "))
credit = float(input("Enter deposit amount: "))

my_checking_account = Checking_Account(cus_name, account_number, address, \
                                       initial_balance)


my_checking_account.credit(credit)
my_checking_account.debit(debit)

print(my_checking_account.to_string())

