#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """ Initializing an instance of ``Rectangle``
        Arguments:
            width (int): The width of new Rectangle.
            height (int): The height of new Rectangle. """
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
        return (self.height * self.width)

    def perimeter(self):
        """Perimeter of the rectangle"""
        return ((self.height * 2) + (self.width * 2))

    def __str__(self):
        """# String of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (('#' * self.width + '\n') * (self.height - 1) +
                    '#' * self.width)
