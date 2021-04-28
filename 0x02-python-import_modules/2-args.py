#!/usr/bin/python3
if __name__ == "__main__":
    import sys

if len(sys.argv) == 1:
    print("0 arguments.")
else:
    i = 1
    print("{:d} arguments:".format((len(sys.argv) - 1)))
    while i < len(sys.argv):
        print("{:d}: {:s}".format(i, sys.argv[i]))
        i += 1
