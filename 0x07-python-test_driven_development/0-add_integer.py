#!/usr/bin/python3
"""
    funtion to add to integers or float
"""


def add_integer(a, b=98):
    """
    add a to b, if b is not specified b is 98 by default
    all floats will be casted to integer
    """

    # validating firts arg (a)    
    if type(a) == int or type(a) == float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    # validating second arg (b)
    if type(b) == int or type(b) == float:
        b = int(b)
    else:
        raise TypeError("b must be an integer")


    return a + b