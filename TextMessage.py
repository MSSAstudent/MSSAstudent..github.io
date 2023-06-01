#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab02, exercise1, Text Message Cost Calculator

# declare variables
messagecount = 0
month = ""
totalcost = 0
pretax = 0
roundedtotal = 0


# input
month = (input("Enter the month the messages were sent: "))
messagecount = int(input("Enter number of messages sent during the month of: "))

# process
pretax = messagecount * 0.25 #cost per message is .25 cents
totalcost = (pretax * .09) + pretax
roundedtotal = round(totalcost, 2)

# output
print("Total cost of messages sent in %s is " % (month) +str(roundedtotal))
