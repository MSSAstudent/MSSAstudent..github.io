#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab08, exercise3, Player_test

from Employee import Employee
from Student import Student


#name = input("Enter employees name: ")
#address = input("Enter employee address: ")
#age = input("Enter employees current age: ")
#job_skills = input("Enter employees primary job skill: ")
#yrw = input("Enter employees years of experiance: ")
#major = input("Enter college Major: ")
#unit_comp = input("Enter number of college units completed: ")

my_employee = Employee("Hank Tank", "123 Flower lane", 65, "Mason", 26)
my_student = Student("Hank Tank", "123 Flower lane", 65, "Underwater basket weaving", 52)

#my_employee = Employee(name, address, age, job_skills, yrw)
#my_student = Student(name, address, age, major, unit_comp)

print(my_employee.to_string())
print(my_student.to_string())



