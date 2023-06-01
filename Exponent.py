#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab04, exercise1, Exponent



# declare variables
number = 0
exponent = 0

# input
number = int(input("Enter a whole number: "))
exponent = int(input("Enter exponent: "))
i = 0
result = 1


# process
while i < exponent:
    result = result * number
    i = i + 1


# output

print("The result is " + str(result))
