#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb = 0
    for i in range(x):
        try:
            nb += 1
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
    print("")
    return (nb)
