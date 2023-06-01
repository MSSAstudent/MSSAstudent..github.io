#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab07, exercise2, Pizza

import Methods as m

class Pizza:
    __sizes = ["Small", "Medium", "Large"]
    __prices = [8.00, 10.00, 12.00]

    def __init__(self, toppings, size, qty):
        self.__price = 0
        self.__toppings = toppings
        self.__qty = qty
        self.set_size(size)

    def get_toppings(self):
        return self.__toppings
    def set__toppings(self, toppings):
        self.__toppings = toppings
    def get_size(self):
        return self.__size
    def set_size(self, size):
        idk = m.find_string(self.__sizes, size)
        if idk >= 0:
            self.__price = self.__prices[idk]
            self.__size = size
        else:
            self.__size = __sizes[0]
            self.__price = __prices[0]
    def get_qty(self):
        return self.__qty
    def set_qty(self, qty):
        if qty < 0:
            qty = 0
        self.__qty = qty

    def calculate_price(self):
        return self.__price * float(self.__qty)

    def to_string(self):
        ext_price = self.calculate_price()
        return "toppings: " + self.__toppings + " Size: "\
               + self.__size + " Qty: " + str(self.__qty) + f" Total price: ${ext_price:.2f}"
