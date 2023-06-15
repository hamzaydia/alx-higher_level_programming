#!/usr/bin/python3
def multiply_list_map(my_list=None, number=0):
    if my_list is None:
        return []

    return [x * number for x in my_list]
