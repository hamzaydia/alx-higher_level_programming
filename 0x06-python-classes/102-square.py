#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Square class init"""
        self.size = size

    @property
    def size(self):
        """Size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size of a square, Checks if positive integer"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of a square"""
        return self.__size * self.__size

    def __eq__(self, other):
        """=="""
        return self.area() == other.area()

    def __ne__(self, other):
        """!="""
        return self.area() != other.area()

    def __lt__(self, other):
        """<"""
        return self.area() < other.area()

    def __le__(self, other):
        """<="""
        return self.area() <= other.area()

    def __gt__(self, other):
        """>"""
        return self.area() > other.area()

    def __ge__(self, other):
        """>="""
        return self.area() >= other.area()
