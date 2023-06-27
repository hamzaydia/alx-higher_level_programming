#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print(int(value))
    except (TypeError, ValueError):
        return False
    return True
