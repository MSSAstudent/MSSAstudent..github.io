#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab09, exercise1, Gas Mileage Calculator revisited

from tkinter import *

def calc_mileage():
    
    # Inputs
    miles = float(txtMiles.get())
    gallons = float(txtGallons.get())
    cost_per_gal = float(txtCostPerGal.get())

    # Process
    mpg = miles / gallons
    total_fuel_cost = gallons * cost_per_gal
    cost_per_mile = total_fuel_cost / miles

    #output
    str_mpg.set("{:.2f}".format(mpg))
    str_cpm.set("${:.2f}".format(cost_per_mile))
    str_tot_fuel_cost.set("${:.2f}".format(total_fuel_cost))

def exit_program():
    frm.destroy()

# form

frm = Tk()
frm.title("Find Your MPG")
frm.geometry('500x200')

lblMiles = Label(frm, text="Miles driven:", height=1, width=12)
lblMiles.grid(row=0, column=0)

txtMiles = Entry(frm, width=8)
txtMiles.grid(row=0, column=1)

lblGallons = Label(frm, text="Gallons purchased:", height=1, width=15)
lblGallons.grid(row=0, column=2)

txtGallons = Entry(frm, width=8)
txtGallons.grid(row=0, column=3)

lblCostPerGal = Label(frm, text="Cost per gallon:", height=1, width=12)
lblCostPerGal.grid(row=0, column=4)

txtCostPerGal = Entry(frm, width=8)
txtCostPerGal.grid(row=0, column=5)

lblTextMPG = Label(frm, text="Your MPG is:", height=1, width=10)
lblTextMPG.grid(row=2, column=0)

str_mpg = StringVar()
lblMPG = Label(frm, text="", height=1, width=10, textvariable=str_mpg)
lblMPG.grid(row=2, column=1)

str_tot_fuel_cost = StringVar()
lblTextTotFuel = Label(frm, text="Total Fuel Cost:", height=1, width=12)
lblTextTotFuel.grid(row=3, column=0)

lblTotFuel = Label(frm, text="", height=1, width=10, textvariable=str_tot_fuel_cost)
lblTotFuel.grid(row=3, column=1)

str_cpm = StringVar()
lblTextCPM = Label(frm, text="Cost per mile:", height=1, width=12)
lblTextCPM.grid(row=4, column=0)

lblCPM = Label(frm, text="", height=1, width=10, textvariable=str_cpm)
lblCPM.grid(row=4, column=1)

btnCalc = Button(frm, text="Calculate!", command=calc_mileage, height=1, width=10)
btnCalc.grid(row=6, column=0)

btnExit = Button(frm, text="All done!", command=exit_program, height=1, width=10)
btnExit.grid(row=7, column=0)


frm.mainloop()






