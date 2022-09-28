#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    index = 0
    updated_list = my_list[:]

    if (len(my_list)) == 0:
        return my_list

    if idx < 0:
        return my_list

    for elem in my_list:
        if index == idx:
            updated_list[index] = element
            return updated_list
        index += 1

    if idx >= index:
        return my_list


'''
#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lcopy = my_list.copy()
    if idx < 0:
        return my_list
    if idx < len(my_list) and idx >= 0:
        lcopy[idx] = element
        return lcopy
        '''
