#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return (a / b)
    except ZeroDivisionError:
        return None
        pass
    finally:
        if b == 0:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(a / b))