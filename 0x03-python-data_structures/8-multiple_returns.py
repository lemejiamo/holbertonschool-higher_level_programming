#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return 0, None

    length = len(sentence)
    firts = sentence[0:1]
    return length, firts
