#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab04, exercise2, Future Value

# import locale to do currency formatting
# export LANG=en_us.UTF-8
import locale
locale.setlocale (locale.LC_ALL, "en-US")

# declare variables
payment = 0.0
years = 0
interest_yearly = 0.0
interest_monthly = 0.0
future_value = 0.0
months = 0
month_num = 1

# message with Python format specifiers
msg = "Month: {0:3d} FV: ${1:.2f} Interest: ${2:.2f}"
interest = 0.0
tot_interest = 0.0


# input
payment = float(input("Enter Monthly payment amount: "))
interest_yearly = float(input("Enter annual interest rate: "))
years = int(input("Enter intestment term in years: "))



# process
interest_monthly = interest_yearly / 100 / 12
months = years * 12

while month_num <= months:
    future_value = (payment + future_value) * (1 + interest_monthly)
    interest = future_value * interest_monthly

    print(msg.format(month_num, future_value, interest))
    month_num += 1

tot_interest = future_value - (months * payment)

# output

print("\n\nTotal interest: ${0:.2f})" .format(tot_interest))
