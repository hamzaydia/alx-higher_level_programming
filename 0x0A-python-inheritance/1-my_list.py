#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """print sorted int list (ascending)"""
        print(sorted(self))
