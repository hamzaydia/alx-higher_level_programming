#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Rectangle class init"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Bigger or equal static method to determine which rectangle is bigger"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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
        return self.height * self.width

    def perimeter(self):
        """Perimeter of the rectangle"""
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """# String of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return ((str(self.print_symbol) * self.width + '\n') *
                    (self.height - 1) + str(self.print_symbol) * self.width)

    def __repr__(self):
        """an eval() compatible representation of the rectangle"""
        return "Rectangle(" + str(self.width) + "," + str(self.height) + ")"

    def __del__(self):
        """Print message when the rectangle is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
