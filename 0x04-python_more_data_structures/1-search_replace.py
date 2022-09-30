#!/usr/bin/python3
""" Replace all occurences of an element by another in a new list """


def search_replace(my_list, search, replace):

    ''' List comprehension using map() and lambda '''

    new_list = list(map(lambda num:
                    replace if num == search else num, my_list))

    return new_list
