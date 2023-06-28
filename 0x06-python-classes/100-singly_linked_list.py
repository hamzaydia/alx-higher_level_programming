#!/usr/bin/python3
"""Singly linked list"""


class Node:
    """Node class"""
    def __init__(self, data, next_node=None):
        """Node class init"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data of a nodee"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Data of a node, Checks the value type"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Next node object"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class"""
    def __init__(self):
        """Singly linked list class init"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a node to the last of the singly linked list"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Join singly linked list values in a string"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
