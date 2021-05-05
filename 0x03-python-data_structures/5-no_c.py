#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return
    i = 0

    for i in range(len(my_string)):
        if ord(my_string[i]) == 67 or ord(my_string[i]) == 99:
            new_string = my_string[:i] + my_string[i+1:]
            return new_string
        i += 1

    return my_string
