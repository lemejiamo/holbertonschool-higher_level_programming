#!/usr/bin/python
""" object is kind of class"""


def inherits_from(obj, a_class):
    if type(obj) == a_class:
        return False
    if isinstance(obj, a_class):
        return True
    else:
        return False
