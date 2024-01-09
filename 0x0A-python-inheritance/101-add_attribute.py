#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """To add new attribute.

    Args:
        obj (any): The object add attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of attribute.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
