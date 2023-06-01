#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab08, exercise2, Racecar class

from Automobile import Automobile

class Racecar(Automobile):
    def __init__(self, vin, make, model, color, hp):
        super().__init__(vin, make, model, color)
        self._hp = hp

    def get_hp(self):
        return self._hp

    def set_hp(self):
        self._hp = hp

    def to_string(self):
        return super().to_string() + "\nRacecar horse power: " \
               + self._hp
