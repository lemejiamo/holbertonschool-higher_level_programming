#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    
    for i in dir(hidden_4):
        if(i[0] != '_'):
            print(i)
