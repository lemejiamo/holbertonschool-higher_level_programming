#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = j = 0
    while (j < x):
        try:
            int(my_list[j])
            print("{:d}".format(my_list[j]), end="")
            j += 1
            i += 1
        except:
            j += 1
    print()
    return i
