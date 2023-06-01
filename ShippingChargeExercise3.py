#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab05, exercise3, Shipping Charge Exercise 

# declare variables
# Arrays
zips = [92020, 91901, 92040, 91976, 92071]
cities = ["El Cajon", "Alpine", "Lakeside", "Spring Valley", "Santee"]
express = ["$5.00", "$10.00", "$7.00", "$6.00", "$7.00"]
ground = ["$3.00", "$5.00", "$4.00", "$3.00", "$4.00"]


# Other variables
zip_code = 0
method = 0
city = "ZIP CODE NOT FOUND"
shipping = ""
found = False
i = 0
list_len = len(zips) 

# input

while True:
    try:
        zip_code = int(input("Enter zip code: "))
        if zip_code < 11111 or zip_code > 99999:
            raise ValueError
        break
    except ValueError:
        print("Not a valid entry. ")

while True:
     try:
        method = int(input("Select shipping method (1 = Express/2 = ground): "))
        if method < 1 or method > 2:
            raise ValueError
        break
     except ValueError:
        print("Invalid entry. Please try again. ")
        
# Search

while i < list_len and not found:
    if zip_code == zips[i]:
       city = cities[i]
       if method == 1:
           shipping = express[i]
       if method == 2:
            shipping = ground[i]
       
       found = True
    i = i + 1

# output

print("Zip: " + str(zip_code) + " City: " + city + " Shipping cost: " + shipping)
