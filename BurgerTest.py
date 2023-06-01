#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab07, exercise4, Burger test

from Burger import Burger

cus_name = str(input("Enter customer name: "))
order_number = str(input("Enter order number: "))
burger = str(input("Enter burger type (Regular, Cheese, Double meat w/Bacon & Cheddar): "))
qty = int(input("Enter how many burgers you would like: "))


my_burger_order = Burger(cus_name, order_number, burger, qty)




print(my_burger_order.to_string())
