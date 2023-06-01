#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab10, exercise1, BaseballPlayer Class revisited

from Player10 import Player
from CustomExceptions import InvalidBattingException

class BaseballPlayer(Player):
    def __init__(self, name, number, position, batting_avg):
        super().__init__(name, number)

        self._position = position
        self.set_batting_avg(batting_avg)

    def get_position(self):
        return self._position
    
    def set_position(self, position):
        self._position = position

    def get_batting_avg(self):
        return self._batting_avg
    
    def set_batting_avg(self, batting_avg):
        
        if batting_avg >= 0.00 and batting_avg <= 1.00:
            self._batting_avg = batting_avg
        else:
            raise InvalidBattingException

    def to_string(self):
        return super().to_string() + " Field Position: " + self._position + \
               " Batting Avg: " + str(self._batting_avg)
    
