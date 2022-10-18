#!/usr/bin/python3
""" Divide elements of a matrix """


def matrix_divided(matrix, div):
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) < 1:
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    for i in matrix:
        if type(i) != list:
            raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")
        length = len(matrix[0])
        if length != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats") 
    TypeError("Each row of the matrix must have the same size")
    return(list(map(lambda i: list(map(
        lambda j: round(j / div, 2), i)), matrix)))
