#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uniques = list(set_1) + list(set_2)
    uniques = list(dict.fromkeys(uniques))
    return uniques
