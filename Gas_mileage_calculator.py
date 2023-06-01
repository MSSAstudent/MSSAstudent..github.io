#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab02, exercise2, Gas Mileage Calculator

# declare variables
fuelAdded = 0
mpg = 0 # mpg = miles per gallon
milesDriven = 0
costPerGallon = 0
costPerMile = 0
totalFuelCost = 0
carMake = ""
finalCostPerMile = 0



# input
carMake = (input("Enter the car's make and model (make, model): "))
milesDriven = float(input("Enter number of miles driven since the last full tank: "))
fuelAdded = float (input ("Enter the amount of fuel added after the drive: "))
costPerGallon = float (input ("Enter the amount paid per gallon: "))

# process
mpg = milesDriven / fuelAdded 
totalFuelCost = costPerGallon * fuelAdded
costPerMile = totalFuelCost / milesDriven
finalCostPerMile = round(costPerMile, 3)

# output
print("***Your %s gets" % (carMake))
print("***Miles Per Gallon " +str (mpg))
print("***The total cost of fuel is $" +str (totalFuelCost)) 
print("***Total cost of fuel per mile is $" +str (finalCostPerMile))  
