#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab07, exercise2, Pizza test

from Pizza import Pizza

toppings = input("Enter toppings: ")
size = input("Enter size (Small, Medium, Large): ")
qty = input("Enter qty: ")

my_pizza = Pizza(toppings, size, qty)

print(my_pizza.to_string())
