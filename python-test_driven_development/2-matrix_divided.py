#!/usr/bin/python3

"""
This module defines a function to divide all elements of a matrix.

The function `matrix_divided` takes a matrix and a divisor,
and returns a new matrix with all elements divided by the divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Parameters:
    matrix (list of lists of int/float): The matrix to be divided.
    div (int/float) is the divisor.

    Returns:
    list of lists of float: the new matrix with all elements divided by div.

    Raises:
    TypeError: If matrix is not a list of lists of integers/float
    TypeError: if each row of the matrix is not of the same size.
    TypeError: if div is not a number(integer or float).
    ZeroDivisionError: If div is zero.
    """
    # verification div est un nombre
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list):
        raise TypeError("matrix must "
            "be a matrix(list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must "
                    "be a matrix(list of lists) of integers/floats")

    # verification que chaque ligne de la matrice a la même taille
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # Verification div pas égal à 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # division de chaque élément de la matrice
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    return new_matrix
