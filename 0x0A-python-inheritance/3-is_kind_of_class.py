#!/usr/bin/python
""" object is kind of class"""


def is_kind_of_class(obj, a_class):
    if type(obj) == a_class:
        return True
    elif isinstance (obj, a_class): 
        return True
    else:
        return False
