#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializes this square class
        Raise TypeError(if size is not integer) or ValueError(if size is less than zero)
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
