#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab08, exercise4, Person Class

from CustomExceptions import InvalidAge

class Person:
    def __init__(self, name, address, age):
        self._name = name
        self._address = address
        self.set_age(age)

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
   
        if age >= 0 and age <= 120:
            self._age = age
        else:
            raise InvalidAge
        


    def to_string(self):
        return "Name: " + self._name \
               + " Home Address: " + self._address \
               + " Age: " + str(self._age)
    
