#!/usr/bin/python3
for num1 in range(0, 9):
    for num2 in range(1, 10):
        if num1 == 8 and num2 == 9:
            print("{}{}".format(num1, num2))
        elif num2 > num1:
            print("{}{}, ".format(num1, num2), end='')
