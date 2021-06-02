#!/usr/bin/python
""" object is kind of class"""


def is_kind_of_class(obj, a_class):
    """ verify if object belongs to given class """

    if type(obj) is a_class:
        return True
    elif isinstance (obj, a_class): 
        return True
    else:
        return False
