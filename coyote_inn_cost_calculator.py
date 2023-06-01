#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab03, exercise3, Coyote Inn

# import locale to do currency formatting
# export LANG=en_us.UTF-8
import locale
locale.setlocale (locale.LC_ALL, "en-US")

# declare variables
month = 0
days = 0
rate = 0
charge = 0.00



# input

while True:
    try:
        month = int(input("What month would you like to stay with us. (enter month number): "))
        if month < 1 or month > 12:
            raise ValueError
        break
    except ValueError:
        print("Not a valid entry. ")
        
days = int(input("How many days would you like to stay: "))

# process
if month == 1 or month == 2 or month == 3:
    rate = 80.00
elif month == 4 or month == 5 or month == 6:
    rate = 90.00
elif month == 7 or month == 8 or month == 9:
    rate = 120.00
else:
    rate = 100

#calculate the rate
charge = rate * days

# output

print("Total cost for your stay: " + locale.currency(charge, grouping=True))
