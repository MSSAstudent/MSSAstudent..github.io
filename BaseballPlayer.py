#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab08, exercise3, BaseballPlayer Class

from Player import Player

class BaseballPlayer(Player):
    def __init__(self, name, number, position, batting_avg):
        super().__init__(name, number)

        self._position = position
        self._batting_avg = batting_avg

    def get_position(self):
        return self._position
    def set_position(self, position):
        self._position = position

    def get_batting_avg(self):
        return self._batting_avg
    def set_batting_avg(self, batting_avg):
        self._batting_avg = batting_avg

    def to_string(self):
        return super().to_string() + " Field Position: " + self._position + \
               " Batting Avg: " + str(self._batting_avg)
    
