#!/usr/bin/python3
""" object is kind of class"""


def is_kind_of_class(obj, a_class):
    """ verify if object belongs to given class """

    if isinstance(obj, a_class):
        return True
    else:
        return False
