#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    mod = ((number * -1) % 10) * -1
else:
    mod = number % 10
str = "Last digit of {:d} is {:d} and {}"
if mod == 0:
    print(str .format(number, mod,  'is 0'))
elif mod > 5:
    print(str .format(number, mod, 'is greater than 5'))
elif mod < 6:
    print(str .format(number, mod, 'is less than 6 and not 0'))
