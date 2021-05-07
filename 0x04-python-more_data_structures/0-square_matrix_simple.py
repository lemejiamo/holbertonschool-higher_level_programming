#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = list(map(lambda x: list(map(lambda num: num * num, x)), matrix))
    return new
