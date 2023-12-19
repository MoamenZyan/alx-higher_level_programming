#!/usr/bin/python3

"""This Module Is For Linked List."""


class Node:
    """Node class for a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): Reference to the next node in the linked list.

    Methods:
        __init__: Initializes a new instance of the Node class.
    """

    def __init__(self, data, next_node=None):
        """Initialize a new instance of the Node class.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): the next node in the linked list.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node.
        """
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")

        if isinstance(next_node, Node) or next_node is None:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """Get the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data in the node.

        Args:
            value (int): The new data to be set.

        Raises:
            TypeError: If the new data is not an integer.
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Get the reference to the next node.

        Returns:
            Node: Reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the reference to the next node.

        Args:
            value (Node or None): The new reference to the next node.

        Raises:
            TypeError: If the new reference is not a Node object or None.
        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object or None")


class SinglyLinkedList:
    """SinglyLinkedList class representing a singly linked list.

    Attributes:
        __head (Node): Reference to the first node in the linked list.

    Methods:
        __init__: Initializes a new instance of the SinglyLinkedList class.
        sorted_insert: Inserts a new node with sorted order into the list.
        __str__: Returns a string representation of the linked list.
    """

    def __init__(self):
        """Initialize a new instance of the SinglyLinkedList class."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node with sorted order into the linked list.

        Args:
            value (int): The data to be stored in the new node.
        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list.

        Returns:
            str: String representation of the linked list.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
