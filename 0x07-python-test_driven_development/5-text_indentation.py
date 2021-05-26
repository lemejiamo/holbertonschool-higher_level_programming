#!/usr/bin/python3
"""
    a function that print a text with 2 new
    lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    this function receives a string as argument
    and ident the text after each of one of this simbols
    (.), (?), (:),

    Attributes

    text: is the string to indent

    """

    # data validation, is a string?
    if type(text) == str:
        i = 0
        while i < (len(text)):
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                print(text[i])
                print()
                i += 2
            else:
                print(text[i], end='')
                i += 1

    # if text is anyother type
    else:
        raise TypeError("text must be a string")
