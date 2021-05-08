#!/usr/bin/python3
def common_elements(set_1, set_2):
    equals = []
    for i in set_1:
        for j in set_2:
            if j == i:
                equals.append(j)
    return equals
