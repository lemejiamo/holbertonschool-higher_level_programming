#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    j = len(my_list) * -1
    i = -1
    while i >= j:
        print("{:d}\n".format(my_list[i]), end='')
        i -= 1
