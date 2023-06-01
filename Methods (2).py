#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab06, exercise1, Method Lib

# contains libaray of methods

def get_float_val(prompt):
    is_num = False
    str_val = input(prompt)
    while is_num == False:
        try:
            value = float(str_val)
            is_num = True
        except:
            print(str_val + " is not a float!")
            str_val = input(prompt)
    return value

#end "get_float_val"

def get_int_val(prompt):
    is_num = False
    str_val = input(prompt)
    while is_num == False:
        try:
            value = int(str_val)
            is_num = True
        except:
            print(str_val + " is not a number!")
            str_val = input(prompt)
    return value

# "is_float"

def is_float(value):
    try:
        num = float(value)
        return True
    except:
        return False

# "is_int"

def is_integer(value):
    try:
        num = int(value)
        return True
    except:
        return False

# "find_string_method"

def find_string(the_list, find_val):
    list_len = len(the_list)
    found = False
    i = 0
    idx = -1
    while i < list_len and found == False:
        if find_val.upper() == the_list[i].upper():
            idx = i
            found = True
        i += 1
    return idx

# "find_int()"

def find_int(num_list, find_val):
    list_len = len(num_list)
    found = False
    i = 0
    idx = -1
    while i < list_len and found == False:
        if find_val.upper() == num_list[i].upper():
            idx = i
            found = True
        i += 1
    return idx


			


