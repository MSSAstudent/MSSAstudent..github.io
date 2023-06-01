#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab08, exercise1, CarTest

from Convertible import Convertible
from Racecar import Racecar

#make = input("Enter make: ")
#model = input("Enter model: ")
#vin = input("Enter VIN: ")
#color = input("Enter color: ")
#yn = input("Is the top up (yes/no): ")

#if yn.upper() == "YES":
    #is_top_up = True
#else:
    #is_top_up = False

#my_car = Convertible(vin, make, model, color, is_top_up)
car1 = Convertible("8675309", "Ford", "T-bird", "Blue", "Yes")
car2 = Convertible("555-3501", "Dodge", "Dart", "Pink", "No")

#print(my_car.to_string())
print(car1.to_string())
print(car2.to_string())

#make = input("Enter make: ")
#model = input("Enter model: ")
#vin = input("Enter VIN: ")
#color = input("Enter color: ")
#hp = input("What is the horsepower rating of your race car?: ")



#my_racecar = Racecar(vin, make, model, color, hp)
racecar1 = Racecar("Matching", "Fast", "Too Fast", "Blur", "760")
racecar2 = Racecar("000001", "International", "Power Wagon", "Wood", "2.5")

#print(my_racecar.to_string())
print(racecar1.to_string())
print(racecar2.to_string())
