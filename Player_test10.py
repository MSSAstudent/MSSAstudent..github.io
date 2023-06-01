#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab10, exercise1, Player_test fixture

from BaseballPlayer10 import BaseballPlayer
from CustomExceptions import InvalidPlayerNumException
from CustomExceptions import InvalidBattingException

try:
    name = input("Enter Baseball player: ")
    number = int(input("Enter Number: "))
    position = input("Enter position: ")
    batting_avg = float(input("Enter batting average: "))

    player = BaseballPlayer(name, number, position, batting_avg)
    print(player.to_string())
    
    # Test data 
    #player1 = BaseballPlayer("Fred", 55, "first base", 378)
    #print(player1.to_string())
    
    #player2 = BaseballPlayer("Wilson", 12, "Third", .276)
    #print(player2.to_string())
    
    # Exception error
    #player3 = BaseballPlayer("Watson", TKO, "Pitcher", .176)
    #print(player3.to_string())
    
    # invalid player number
    #player4 = BaseballPlayer("Willis", -1, "Third", .276)
    #print(player4.to_string())
    
    # Invalid Batting AVG
    #player5 = BaseballPlayer("Ham", 56, "RF", 7)
    #print(player5.to_string())
    
except InvalidPlayerNumException as e:
    print("Invalid Player Number! Valid numbers are between 1 and 9999. ", e)
except InvalidBattingException as e:
    print("Invalid Batting Average! Valid entry are between 0 and 1. ", e)
except Exception as ex:
    print("Generic exception: ", ex)




