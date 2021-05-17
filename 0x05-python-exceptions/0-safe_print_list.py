#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    while (j < x):
        try:
            print("{}".format(my_list[j]), end="")
            j += 1
        except:
            print()
            return j
    print()
    return j
