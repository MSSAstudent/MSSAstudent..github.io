#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab03, exercise2, BMI calculator

            
# declare variables
message = ""
bmi = 0.0
pounds = 0
inches = 0
kilograms = 0
meters = ""



# input
inches = int(input("Enter height in inches: "))
pounds = int(input("Enter weight in pounds: "))

# process
#BMI calculator
meters = inches / 39.36
kilograms = pounds / 2.2
bmi = kilograms / meters**2


#message selection
if bmi <= 18.4:
    message = "Underweight"
elif bmi >= 18.5 and bmi <= 24.99:
    message = "Normal weight"
elif bmi >= 25 and bmi <= 29.99:
    message = "Overweight"
elif bmi >= 30 and bmi <= 39.99:
    message = "Obese"
else:
    message = "Morbid Obesity"



# output
print("Weight: " + str (pounds))
print("Height: " + str (inches))
print("Your BMI is: %.2f" % (bmi))
print("Your current Body Mass Index indicates you are: " + message)
