#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab04, exercise1.1, Factorial



# declare variables
factorial = 0
i = 1
result = 1



# input
factorial = int(input("Enter whole number: "))


# process
for i in range(1, factorial + 1, 1):
    result = result * i

# output

print("The result is " + str(result))
