#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        mod = (number * -1) % 10
    else:
        mod = number % 10
    print("{:d}".format(mod), end='')
    return mod
