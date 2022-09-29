#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    if len(my_list) == 0:
        return None
    maxNumber = my_list[-1]
    for elements in my_list:
        if elements > maxNumber:
            maxNumber = elements
    return maxNumber
