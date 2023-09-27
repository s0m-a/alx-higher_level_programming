#!/usr/bin/python3
"""Node Class"""


class Node:
    """Defines a node of a linked list"""
    def __init__(self, data, next_node=None):
        """Interior data of node
        Args:
            data (int): content of node
        Returns: None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Takes the data
        Args:
            data (int): node content
        Returns: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ Handle data errs
        Args:
            data (int): node content
        """
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        """getting next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ next setter """
        if value is None:
            self.__next_node = value
            return
        if type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next must be a Node object")


"""SLL Class"""


class SinglyLinkedList:
    """
     Vars and Methods of the SLLClass
    """
    def __init__(self):
        """ sets inits """
        self.__head = None

    def sorted_insert(self, value):
        """ inserts node in position"""
        temp = self.__head
        new_node = Node(value, self.__head)
        if temp is None:
            self.__head = new_node
            return
        if temp.data > value:
            new_node.next_node = temp
            self.__head = new_node
            return
        while temp.next_node is not None:
            if temp.next_node.data > value:
                break
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node
        return

    def __str__(self):
        """ creates str representation """
        new_list = []
        temp = self.__head
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next_node
        string = '\n'.join(str(item) for item in new_list)
        return string
