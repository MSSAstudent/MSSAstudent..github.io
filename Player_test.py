#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab08, exercise3, Player_test

from BaseballPlayer import BaseballPlayer
from BasketballPlayer import BasketballPlayer

#name = input("Enter Baseball player: ")
#number = int(input("Enter Number: "))
#position = input("Enter position: ")
#batting_avg = float(input("Enter batting average: "))

# my_player = BaseballPlayer(name, number, position, batting_avg)
player1 = BaseballPlayer("Fred", 55, "first base", 3.78)
player2 = BaseballPlayer("Wilson", 00, "Third", 2.76)

#print(my_player.to_string())
print(player1.to_string())
print(player2.to_string())

#name = input("Enter Basketball player: ")
#number = int(input("Enter Number: "))
#position = input("Enter position: ")
#freeThrow_pct = float(input("Enter free throw percentage: "))

# my_player = BasketballPlayer(name, number, position, freeThrow_pct)
bball1 = BasketballPlayer("jones", 24, "Center ", 50.2)
bball2 = BasketballPlayer("smith", 25, "FWD ", 78)
#print(my_player.to_string())
print(bball1.to_string())
print(bball2.to_string())
