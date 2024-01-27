def print_square(size):
    """ Print a square using # size x size """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
    for _ in range(size):
        print('#' * size)
