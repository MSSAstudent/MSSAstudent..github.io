#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab10, exercise1, Player Class Revisited implementation

from CustomExceptions import InvalidPlayerNumException

class Player:
    def __init__(self, name, number):
        self._name = name
        self.set_number (number)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_number(self):
        return self._number

    def set_number(self, number):
        MIN_NUMBER = 1
        MAX_NUMBER = 9999

        if number >= MIN_NUMBER and number <= MAX_NUMBER:
            self._number = number
        else:
            raise InvalidPlayerNumException

    def to_string(self):
        return "Name: " + self._name + " Number: " + str(self._number)
    
