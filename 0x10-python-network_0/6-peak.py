#!/usr/bin/python3
""" find a peak in a list """


def find_peak(list_of_integers):
    """ find a peak into a list"""
    if list_of_integers == []:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
