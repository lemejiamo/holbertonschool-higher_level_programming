#!/usr/bin/python3
""" find a peak in a list """

def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    sorted_list = []
    sorted_list = sorted(list_of_integers)
    peak = (sorted_list[-1])
    return peak
