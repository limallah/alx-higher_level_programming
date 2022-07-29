#!/usr/bin/python3
"""class Rectangle with the Area and Perimeter"""


class Rectangle:
    """creates a class Rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initializes an object imediately it is created
        Arg: width and height which must be an integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """creates a private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the private instance attributes width to a value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the private instance attributes height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets a value to height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instance method that returns the area of the object"""
        rectangle_area = self.height * self.width
        return rectangle_area

    def perimeter(self):
        """public instance method that returns the perimeter of the object"""
        if (self.__height == 0) or (self.width == 0):
            rectangle_perimeter = 0
        else:
            rectangle_perimeter = 2 * (self.height + self.width)
        return rectangle_perimeter

    def __str__(self):
        """
        Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if (self.__height == 0) or (self.width == 0):
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append("#") for j in range(self.__width)]
            if i != self.height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Tye rectangle's string representation"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)
