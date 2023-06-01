#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab04, exercise3, Heads or Tails

# import random
import random




# declare variables
max_flips = 20
max_val = 2
heads = 0.0
tails = 0.0
pct_heads = 0.0
pct_tails = 0.0
i = 0
flip = 0


# input
# for testing change max_flips to 0 and change the line below from
# a note to an input.
# max_flips = int(input("Enter number of flips: "))



# process
for i in range(1, max_flips +1):
    flip = random.randint(0,1)
    if flip == 0:
        heads = heads + 1
        print("%d. Heads" % (i))
    if flip == 1:
        tails = tails + 1
        print("%d. Tails" % (i))
    i = i + 1
   
     

pct_heads = (heads / max_flips) * 100.0
pct_tails = (tails / max_flips) * 100.0



# output

print("Total Heads: {0}".format(heads))
print("Total Tails: {0}".format(tails))
print("Percent Heads: %{0:.1f}".format(pct_heads))
print("Percent Tails: %{0:.1f}".format(pct_tails))
