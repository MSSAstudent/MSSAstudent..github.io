#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab08, exercise1, Convertible class

from Automobile import Automobile

class Convertible(Automobile):
    def __init__(self, vin, make, model, color, is_top_up):
        super().__init__(vin, make, model, color)
        self._is_top_up = is_top_up

    def get_is_top_up(self):
        return self._is_top_up

    def set_is_top_up(self):
        self._is_top_up = is_top_up

    def fmt_top_status(self):
        status = "No"
        if self._is_top_up == True:
            status = "yes"
        return status

    def to_string(self):
        return super().to_string() + "\nIs top up? " + self.fmt_top_status()
