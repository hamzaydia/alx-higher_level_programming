#!/usr/bin/python3
'''Module with lookup function'''

def lookup(obj):
    '''Return list of obj attrs & methds availble'''
    return dir(obj)
