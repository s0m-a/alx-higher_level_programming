#!/usr/bin/python3
"""Defines a matrix division function."""
def matrix_divided(matrix, div):
    s = 'matrix must be a matrix (list of lists) of\
 integers/floats'
    if not matrix or type(matrix) is not list:
        raise TypeError(s)
    for r in matrix:
        if type(r) is list and r:
            for x in r:
                if type(x) is not int and type(x) is not float:
                    raise TypeError(s)
        else:
            raise TypeError(s)

    rsize = len(matrix[0])
    for r in matrix:
        if len(r) != rsize:
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    matrix2 = list(map(list, matrix))
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix2[r][c] = round(matrix[r][c] / div, 2)
    return matrix2
