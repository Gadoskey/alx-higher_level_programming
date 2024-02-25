#!/usr/bin/python3
# Author -- Gadoskey
"""
    A class Square that inherits class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Class Square that inherits Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initialises Square
        """
        super().__init__(size, size, x, y, id)

        """Call superclass constructor with appropriate arguments
            with width and height assigned the value of size
        """

    @property
    def size(self):
        """
            returns the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            sets the value of size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(key, value)

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
            Overloading str function
        """
        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Square
        """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
