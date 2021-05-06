#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return
    
    new_string = my_string.translate({ord(i):'' for i in "Cc"})
    return (new_string)