#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab05, exercise1, Array Search

# declare variables
# Arrays
zips = [53115, 53125, 53147, 53184]
cities = ["Delevan", "Fontana", "Lake Geneva", "Walworth"]
states = ["WI", "WI", "IL", "IL"]

# Other variables
zip_code = 0
city = "NOT FOUND"
state = ""
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
        
# Search
while i < list_len and not found:
    if zip_code == zips[i]:
       city = cities[i]
       state = states[i]
       found = True
    i = i + 1

# output

print("Zip: " + str(zip_code) + " City: " + city + " State: " +state)
