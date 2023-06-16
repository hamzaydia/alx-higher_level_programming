#!/usr/bin/python3
def print_list_integer(my_list=None):
    if my_list is None:
        my_list = []
    print('\n'.join(f'{i:d}' for i in my_list))
