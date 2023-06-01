#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab09, exercise2, BMI calculator GUI

from tkinter import *

def calc_bmi():
    
    # Inputs
    height = float(txtHeight.get())
    weight = float(txtWeight.get())


    # Process
    meters = height / 39.36
    kilograms = weight / 2.2
    bmi = kilograms / meters**2

    #message selection
    if bmi <= 18.4:
        message = "Underweight!"
    elif bmi >= 18.5 and bmi <= 24.99:
        message = "Normal weight!"
    elif bmi >= 25 and bmi <= 29.99:
        message = "Overweight!"
    elif bmi >= 30 and bmi <= 39.99:
        message = "Obese!"
    else:
        message = "Morbid Obesity"

    #output
    str_bmi.set("{:.2f}".format(bmi))
    str_message.set(message)
    

def exit_program():
    frm.destroy()

frm = Tk()
frm.title("    **    BMI Calculator    **    ")
frm.geometry('300x200')
# Height input
lblHeight = Label(frm, text="Height in inches: ", height=2, width=15)
lblHeight.grid(row=0, column=0)

txtHeight = Entry(frm, width=8)
txtHeight.grid(row=0, column=1)
# Weight input
lblWeight = Label(frm, text="Weight in pounds: ", height=2, width=15)
lblWeight.grid(row=1, column=0)

txtWeight = Entry(frm, width=8)
txtWeight.grid(row=1, column=1)
# output BMI
lblTextBMI = Label(frm, text="Your BMI is: ", height=2, width=15)
lblTextBMI.grid(row=2, column=0)

str_bmi = StringVar()
lblBMI = Label(frm, text="", height=1, width=10, textvariable=str_bmi)
lblBMI.grid(row=2, column=1)
# output message
lblTextMessage = Label(frm, text="BMI catagory is: ", height=2, width=15)
lblTextMessage.grid(row=3, column=0)

str_message = StringVar()
lblMessage = Label(frm, text="", height=1, width=10, textvariable=str_message)
lblMessage.grid(row=3, column=1)
# buttons
btnCalc = Button(frm, text="Calculate", command=calc_bmi, height=1, width=15)
btnCalc.grid(row=6, column=0)

btnExit = Button(frm, text="Finished!", command=exit_program, height=1, width=15)
btnExit.grid(row=6, column=1)


frm.mainloop()
