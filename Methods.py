#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab012, exercise1, sort_integers

# Sort methods

def de_sort_integers(num_list):
    x = 1
    list_len = len(num_list)
    while x < list_len:
        temp = num_list[x]
        y = x - 1
        while y >= 0 and num_list[y] < temp:
            num_list[y + 1] = num_list [y]
            y = y - 1
        #end while
        num_list[y + 1] = temp
        x = x + 1
    #end while
    return num_list

def as_sort_integers(num_list):
    x = 1
    list_len = len(num_list)
    while x < list_len:
        temp = num_list[x]
        y = x - 1
        while y >= 0 and num_list[y] > temp:
            num_list[y + 1] = num_list [y]
            y = y - 1
        #end while
        num_list[y + 1] = temp
        x = x + 1
    #end while
    return num_list

def calc_median(num_list):
    mid = len(num_list) // 2
    result = (num_list[mid] + num_list[~mid])/2
    return result
    

def calc_mean(num_list):
    x = len(num_list)
    total = sum(num_list)
    
    mean = total / x

    return mean

        
