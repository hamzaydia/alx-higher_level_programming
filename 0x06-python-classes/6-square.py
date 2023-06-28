#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Square class init"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size of a square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Size of a square, checks if size is positive"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Position of a square"""
        return self.__position

    @position.setter
    def position(self, size):
        if (not isinstance(size, tuple) or
                len(size) != 2 or
                not all(isinstance(n, int) for n in size) or
                not all(n >= 0 for n in size)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = size

    def area(self):
        """Area of a square"""
        return self.__size ** 2

    def my_print(self):
        """Print square using #"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
