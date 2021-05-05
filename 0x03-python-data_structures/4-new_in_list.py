#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0):
        return my_list
    if (len(my_list) - 1) < idx:
        return my_list
    if not my_list:
        return 
    # create a empty list
    copy_list = []
    # add the elemtes from my_list to empty list
    copy_list.extend(my_list)
    copy_list[idx] = element
    return copy_list
