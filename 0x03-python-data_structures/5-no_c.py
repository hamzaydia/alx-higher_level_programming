#!/usr/bin/python3
def no_c(s):
    result = ''
    for i in s:
        if i != 'c' and i != 'C':
            result += i
    return result
