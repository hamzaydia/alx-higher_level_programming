#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    r = []
    d = 0
    if (isinstance(my_list_1, list) and isinstance(my_list_2, list) and
            isinstance(list_length, int)):
        for i in range(list_length):
            try:
                d = my_list_1[i] / my_list_2[i]
            except TypeError:
                print("wrong type")
            except ZeroDivisionError:
                print("division by 0")
            except IndexError:
                print("out of range")
            finally:
                r.append(d)
                d = 0
    return r
