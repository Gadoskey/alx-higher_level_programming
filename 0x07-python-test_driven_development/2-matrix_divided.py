#Author -- Gadoskey
#!/usr/bin/python3
"""

This module is composed by a function that divides the numbers of a matrix

"""

def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix are not lists
                   If the elemetns of the lists are not integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero

    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    message1 = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(message1)

    length = 0
    message2 = "Each row of the matrix must have the same size"

    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(message1)

        if length != 0 and len(row) != length:
            raise TypeError(message2)

        for items in row:
            if not type(items) in (int, float):
                raise TypeError(message1)

        length = len(element)

    new_matrix = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (new_matrix)
