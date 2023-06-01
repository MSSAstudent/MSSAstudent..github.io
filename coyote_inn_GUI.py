#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab09, exercise3, Coyote Inn GUI

from tkinter import *


def calc_rate():
    # Inputs
    month = int(txtMonth.get())
    days = int(txtDays.get())

    # process

    if month == 1 or month == 2 or month == 3:
        rate = 80.00
    elif month == 4 or month == 5 or month == 6:
        rate = 90.00
    elif month == 7 or month == 8 or month == 9:
        rate = 120.00
    else:
        rate = 100

    #calculate the rate
    total = rate * days

     #output
    str_rate.set("${:.2f}".format(rate))
    str_total.set("${:.2f}".format(total))



def exit_program():
    frm.destroy()

 

frm = Tk()
frm.title("Coyote INN reservation system")
frm.geometry('350x350')

# Inputs
lblMonth = Label(frm, text="What month would you like to stay?:", height=2, width=30)
lblMonth.grid(row=0, column=0)

txtMonth = Entry(frm, width=8)
txtMonth.grid(row=0, column=1)

lblDays = Label(frm, text="How many days would you like to stay?:", height=2, width=30)
lblDays.grid(row=1, column=0)

txtDays = Entry(frm, width=8)
txtDays.grid(row=1, column=1)

# output

str_rate = StringVar()
lblTextRate = Label(frm, text="Nightly Rate:", height=2, width=30)
lblTextRate.grid(row=2, column=0)

lblRate = Label(frm, text="", height=1, width=10, textvariable=str_rate)
lblRate.grid(row=2, column=1)

str_total = StringVar()
lblTextTotal = Label(frm, text="Total Cost:", height=2, width=30)
lblTextTotal.grid(row=3, column=0)

lblTotal = Label(frm, text="", height=1, width=10, textvariable=str_total)
lblTotal.grid(row=3, column=1)


# buttons
btnFind = Button(frm, text="Find Rate!", command=calc_rate, height=1, width=12)
btnFind.grid(row=6, column=0)

btnExit = Button(frm, text="Finished!", command=exit_program, height=1, width=12)
btnExit.grid(row=6, column=1)


frm.mainloop()
