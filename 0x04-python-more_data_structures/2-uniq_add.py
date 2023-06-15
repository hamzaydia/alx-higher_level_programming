#!/usr/bin/python3
def uniq_add(my_list=None):
    if my_list is None:
        return 0

    summ = 0
    unique_elements = set()
    for x in my_list:
        if x not in unique_elements:
            summ += x
            unique_elements.add(x)
    return summ
