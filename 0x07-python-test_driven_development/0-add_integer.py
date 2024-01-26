"""
This module provides a function for adding two integers or floats.
The add_integer function takes two arguments, 'a' and 'b', both of which can be integers or floats.
It returns the sum of 'a' and 'b' as integers.
"""

def add_integer(a, b=98):
    """Add two integers.
    Parameters: a (int or float), b (int or float, default 98), Returns: int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
