#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab08, exercise1, Automobile Class 

class Automobile:
    def __init__(self, vin, make, model, color):
        self._vin = vin
        self._make = make
        self._model = model
        self._color = color

    def get_vin(self):
         return self._vin

    def set_vin(self, vin):
        self._vin = vin

    def get_make(self):
         return self._make

    def set_make(self, make):
        self._make = make

    def get_model(self):
         return self._model

    def set_model(self, model):
        self._model = model

    def get_color(self):
         return self._color

    def set_color(self, color):
        self._color = color

    def to_string(self):
        return "VIN#: " + self._vin + " Make: " + self._make + " Model: " \
               + self._model + " Color: " + self._color
         
