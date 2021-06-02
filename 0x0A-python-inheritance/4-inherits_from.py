#!/usr/bin/python3
""" object is kind of class"""


def inherits_from(obj, a_class):
    """ verify if a object is inherit from a given class """

    if type(obj) == a_class:
        return False

    if isinstance(obj, a_class):
        return True

    else:
        return False
