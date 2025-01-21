#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        line = ""
        for i, num in enumerate(row):
            if i > 0:
                line += " "
            line += "{:d}".format(num)
        print(line)
