#!/usr/bin/python3
"""My Function."""


def inherits_from(obj, a_class):
    """Check if object is subclass of a class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
