#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab05, exercise2, Dice Exercise

import random

# variables and constants
MAX_ROLLS = 5
MAX_DICE_VAL = 6

# declare lists for roll types
roll_types = ["Junk", "Pair", "3 of a kind", "4 of a kind", "5 of a kind"]

# declare lists for dice rolls, and tallying up the dice rolls
pdice = [0,0,0,0,0]
cdice = [0,0,0,0,0]

# tally lists will be 6 in size since dice values run from 1 - 6
ptally = [0,0,0,0,0,0]
ctally = [0,0,0,0,0,0]

# roll the dice for player and computer
i = 0
while i < MAX_ROLLS:
    roll_val = random.randint(1,MAX_DICE_VAL)
    pdice[i] = roll_val
    roll_val = random.randint(1,MAX_DICE_VAL)
    cdice[i] = roll_val
    i += 1

# display what the player rolled
i = 0
print("Player rolled: ", end=" ")
while i < MAX_ROLLS:
    print(pdice[i], end=" ")
    i += 1

# display what the computer rolled
i = 0
print("\nComputer rolled: ", end=" ")
while i < MAX_ROLLS:
    print(cdice[i], end=" ")
    i += 1

# Determine pairs, 3 of, 4 of, and 5 of a kind by loading the tally

i = 0
while i < MAX_ROLLS:
    ptally[ pdice[i] -1] += 1
    ctally[ cdice[i] -1] += 1
    i += 1

pmax = ptally[0]
cmax = ctally[0]
i = 1

while i < MAX_DICE_VAL:
    if pmax < ptally[i]:
        pmax = ptally[i]
    

    if cmax < ctally[i]:
        cmax = ctally[i]  
    i += 1


# output - display pairs, 3 of, 4 of, and 5 of a kind by loading the tally
print("\nPlayer rolled: " + roll_types[pmax - 1] )
print("Computer rolled: " + roll_types[cmax - 1] )

# determine teh winner
if pmax > cmax:
    print("player wins!")
elif cmax > pmax:
    print("Computer wins!")
else:
    print("TIE!")
    





    


