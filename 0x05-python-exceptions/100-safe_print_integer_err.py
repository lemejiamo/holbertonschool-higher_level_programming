#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        int(value)
        print("{:d}".format(value))
        return True
    except:
        return False
