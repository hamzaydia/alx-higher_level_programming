#!/usr/bin/python3
""" Module for MyInt class """


class MyInt(int):
    """ MyInt class """

    def __eq__(self, value):
        """Override == with != """
        return self.real != value

    def __ne__(self, value):
        """Override != with == """
        return self.real == value
