#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    i = 0
    while i < length:
        c = ord(str[i])
        if c >= 97 and c <= 122:
            c = c - 32
        print("{:c}".format(c), end='')
        i += 1
    print()
