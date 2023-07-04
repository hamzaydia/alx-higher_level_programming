#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Rectangle class init"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Perimeter of the rectangle"""
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """# String of the rectangle"""
        if self.width is 0 or self.height is 0:
            return ""
        else:
            return (('#' * self.width + '\n') * (self.height - 1) +
                    '#' * self.width)

    def __repr__(self):
        """an eval() compatible representation of the rectangle"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
