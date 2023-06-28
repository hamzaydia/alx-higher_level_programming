#!/usr/bin/python3


def magic_calculation(a, b):
    f = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                f += (a ** b / i)
        except Exception as Exc:
            f = b + a
            break
    return f
