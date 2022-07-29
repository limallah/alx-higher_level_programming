#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """creates a class Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle
        Args:
        width -> must be an integer
        height -> must be an integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width, a private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the private instance width to a value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets a value to height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
