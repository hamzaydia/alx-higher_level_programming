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
    def size(self, size):
        """Size of a square, with positive only test"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of a square"""
        return self.__size ** 2
