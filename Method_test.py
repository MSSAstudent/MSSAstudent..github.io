#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab06, exercise1, Method test

import Methods as m

def main():
    #test library of methods
    float_val = m.get_float_val("Enter a floating point: ")
    print("float value (from our method) " + str(float_val) + " was entered")

    int_val = m.get_int_val("Enter a valid integer: ")
    print("integer (returned from method) " + str(int_val) + " was entered")

    str_val = input("Enter another float: ")
    result = m.is_float(str_val)
    if result == True:
        print(str_val + " is a float")
    else:
        print( str_val + " is not a float")

    int_val = input("Enter another integer: ")
    result = m.is_integer(int_val)
    if result == True:
        print(int_val + " is a integer")
    else:
        print( int_val + " is not a integer")

    my_list = burgers = ["Regular", "Cheese", "Double meat", "Double meat w/Bacon & Cheddar"]
    value = input("Enter a value to find: ")

    idx = m.find_string(my_list, value)
    if idx >= 0:
        print("Found " + value + " at index " + str(idx))
    else:
        print( value + " NOT FOUND!")

    num_list = ["16", "32", "64", "128", "256", "512"]
    value = input("Enter computer memory size 16GB or greater: ")

    idx = m.find_int(num_list, value)
    if idx >= 0:
        print("Found " + value + "GB" + " at index " + str(idx))
    else:
        print( value + " NOT FOUND!")

if __name__ == "__main__":
    main()
