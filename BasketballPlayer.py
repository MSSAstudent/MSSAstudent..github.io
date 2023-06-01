#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab08, exercise4, BasketballPlayer Class

from Player import Player

class BasketballPlayer(Player):
    def __init__(self, name, number, position, freeThrow_pct):
        super().__init__(name, number)

        self._position = position
        self._freeThrow_pct = freeThrow_pct

    def get_position(self):
        return self._position
    def set_position(self, position):
        self._position = position

    def get_freeThrow_pct(self):
        return self._freeThrow_pct
    def set_freeThrow_pct(self, freeThrow_pct):
        self._freeThrow_pct = freeThrow_pct

    def to_string(self):
        return super().to_string() + " Court Position: " + self._position + \
               "Free Throw percentage: " + str(self._freeThrow_pct)
