#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab07, exercise4, Burger

import Methods as m

class Burger:
    __burgers = ["Regular", "Cheese", "Double meat", "Double meat w/Bacon & Cheddar"]
    __costs = [1.75, 2.00, 3.50, 4.50]
    
    def __init__(self, cus_name, order_number, burger, qty):
        
        self.__cus_name = cus_name
        self.__order_number = order_number
        self.set_burger(burger)
        self.__qty = qty
       
       
    def get_cus_name(self):
        return self.__cus_name
    def set_cus_name(self, cus_name):
        self.__cus_name = cus_name
        
    def get_order_number(self):
        return self.__order_number
    def set_order_number(self, order_number):
        self.__order_number = order_number
 
    def get_burger(self):
        return self.__burger
    def set_burger(self, burger):
        idk = m.find_string(self.__burgers, burger)
        #print("IDK: " + str(idk))
        if idk >= 0:
            self.__cost = self.__costs[idk]
            self.__burger = burger
            #print(" cost: " + str(self.__cost))
        else:
            self.__burger = __burgers[0]
            self.__cost = __costs[0]
            
    def get_qty(self):
        return self.__qty




    def calculate_cost(self):
        return self.__cost * self.__qty



    def to_string(self):
        ext_price = self.calculate_cost()       
        
        return "Customer name: " + self.__cus_name + "    - Order number: " + self.__order_number \
        + "    - Burger type: " + self.__burger \
        + "    - Number of burgers ordered: " + str(self.__qty)  \
        + f"    - Your purchase total is: ${ext_price:.2f}"
                                                                                
