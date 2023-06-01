#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab06, exercise2, Coyote Tours

import Methods as m

tour_num = ["1001", "1002", "1003", "1004", "1005"]
destination = ["Mars", "Earths core", "Pluto", "Saturn", "32nd ST & West Highlands"]
cost = [171.88, 39.58, 324.06, 983.66, 5.99]

while True:
    try:
        tour = int(input("What tour would you like to take. (enter tour number): "))
        if tour < 1001 or tour > 1005:
            raise ValueError
        break
    except ValueError:
        print("Not a valid tour number. ")
        
idx = m.find_int(tour_num, str(tour))
if idx >= 0:
    print("Found tour " + str(tour))
if idx >= 0:
    location = destination[idx]
    price = cost[idx]
else:
    print( str(tour) + " NOT FOUND! Please Enter a vaild tour number")
    
party = m.get_int_val("How many people are in your party: ")

sub = price * party
tax = sub * .075
total = tax + sub
total_rounded = "{:.2f}".format(total)
tax_rounded = "{:.2f}".format(tax)

print("   ")
print("A tour of " + location + " for a party of: " + str(party))
print("Rate: $"  + str(price) + " per person." + " Taxes: $" + str(tax_rounded))
print("Total cost is: $" + str(total_rounded)) 


  




