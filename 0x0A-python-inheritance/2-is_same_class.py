#!/usr/bin/python3
""" verify if a object
belongs to a given class """


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
