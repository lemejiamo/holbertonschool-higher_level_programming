#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        int(value)
        print("{:d}".format(value))
        return True
    except (SyntaxError, ValueError):
        sys.stderr.write(value)
        return False
