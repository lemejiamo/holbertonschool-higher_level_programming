#!/usr/bin/python3
import sys

def safe_print_integer_err(value):

    try:
        int(value)
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError)  as err:
        #print(err, file=sys.stderr)
        return False
