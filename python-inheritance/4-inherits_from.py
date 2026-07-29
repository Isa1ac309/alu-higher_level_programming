#!/usr/bin/python3
"""Module for inherits_from."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited from a_class."""
    return type(obj) is not a_class and isinstance(obj, a_class)
