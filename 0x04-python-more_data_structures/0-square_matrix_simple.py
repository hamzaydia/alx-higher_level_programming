#!/usr/bin/python3
def square_matrix_simple(matrix=None):
    if matrix is None:
        return []

    return [[x**2 for x in row] for row in matrix]
