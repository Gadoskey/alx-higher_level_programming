#!/usr/bin/python3
"""A module that defines a square """
class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializes the square class
        Args:
            size: the size
        Raises:TypeError if size is not integer or ValueError if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Gets the size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates area of the square
        Returns: The square of the private instance[size]
        """
        return (self.__size ** 2)
