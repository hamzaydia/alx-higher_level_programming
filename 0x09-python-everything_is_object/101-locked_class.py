#!/usr/bin/python3
""" Module for locked class."""


class LockedClass:
    """ Prevent the user from making new Locked Class attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
