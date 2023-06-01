#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab08, exercise3, Player_test

from Employee10 import Employee
from Student10 import Student
from CustomExceptions import InvalidAge
from CustomExceptions import InvalidYearsWorked
from CustomExceptions import InvalidUnits

try:
    name = input("Enter employees name: ")
    address = input("Enter employee address: ")
    age = int(input("Enter employees current age: "))
    job_skills = input("Enter employees primary job skill: ")
    yrw = int(input("Enter employees years of experiance: "))
    major = input("Enter college Major: ")
    unit_comp = int(input("Enter number of college units completed: "))

    my_employee = Employee(name, address, age, job_skills, yrw)
    my_student = Student(name, address, age, major, unit_comp)

    # Age test
    #my_employee = Employee("Hank Tank", "123 Flower lane", 125, "Mason", 20)
    #my_student = Student("Hank Tank", "123 Flower lane", 125, "Underwater basket weaving", 20)

    # Years worked test
    #my_employee = Employee("Hank Tank", "123 Flower lane", 65, "Mason", 76)
    #my_student = Student("Hank Tank", "123 Flower lane", 65, "Underwater basket weaving", 20)

    
    # Unit test
    #my_employee = Employee("Hank Tank", "123 Flower lane", 65, "Mason", 20)
    #my_student = Student("Hank Tank", "123 Flower lane", 65, "Underwater basket weaving", -2)



    print(my_employee.to_string())
    print(my_student.to_string())


except InvalidAge as e:
    print("Invalid age entered! Valid age is between 0 and 120. ", e)
except InvalidYearsWorked as e:
    print("Invalid number of years worked! Valid entries are between 0 and 75. ", e)
except InvalidUnits as e:
    print("Invalid number of College units entered! Enter units between 0 and 200. ", e)
