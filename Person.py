#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab08, exercise4, Person Class 

class Person:
    def __init__(self, name, address, age):
        self._name = name
        self._address = address
        self._age = age

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address
    def set_address(self, address):
        self._address = address

    def get_age(self):
        return self._age
    def set_age(self, age):
      

        if age >= 1 and age <= 125:
            self._age = age
        else:
            self._age = 9999
        


    def to_string(self):
        return "Name: " + self._name \
               + " Home Address: " + self._address \
               + " Age: " + str(self._age)
    
