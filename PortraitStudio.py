#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab03, exercise1, Portrait Studio

# import locale to do currency formatting
# export LANG=en_us.UTF-8
import locale
locale.setlocale (locale.LC_ALL, "en-US")

# declare variables
surcharge = 1.2
sunday = 1
saturday = 7
base_price = 0.0
day_of_week = 0
last_name = ""
num_subjects = 0


# input
last_name = (input("Enter customers last name: "))
num_subjects = int(input("Enter customer party size: "))
day_of_week = int(input("Day of the week (1 = Sun, 2 = Mon, 3 = Tue, 4 = Wed, 5 = Thur, 6 = Fri, 7 = Sat: "))

# process
if num_subjects == 1:
    base_price = 100
elif num_subjects ==2:
    base_price = 130
elif num_subjects ==3:
    base_price = 150
elif num_subjects ==4:
    base_price = 165
elif num_subjects ==5:
    base_price = 175
elif num_subjects ==6:
    base_price = 180
else:
    base_price = 185

# add surcharge for weekend sitting
if day_of_week == 1 or day_of_week == 7:
    base_price = base_price * surcharge

# output
print("Last name: " + last_name)
print("Total price: " + locale.currency(base_price, grouping=True))
