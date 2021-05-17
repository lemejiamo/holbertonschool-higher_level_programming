#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        print("{}".format(message))
        raise TypeError
    except:
        pass
