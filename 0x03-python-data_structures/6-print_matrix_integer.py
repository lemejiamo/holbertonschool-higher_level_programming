#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print()
        return
    j = 0
    while j < len(matrix):
        i = 0
        while i < (len(matrix[j]) - 1):
            print("{:d}".format(matrix[j][i]), end=' ')
            i += 1
        print("{:d}".format(matrix[j][i]), end='')
        j += 1
        print()
