#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    numbers = [0, 0, 0, 0]
    j = 0
    while j < 2:
        if j < len(tuple_a):
            numbers[j] = tuple_a[j]
        if j < len(tuple_b):
            numbers[j + 2] = tuple_b[j]
        j += 1
    new_tuple = (numbers[0] + numbers[2], numbers[1] + numbers[3])
    return new_tuple
