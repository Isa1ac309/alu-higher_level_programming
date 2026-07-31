#!/usr/bin/python3
"""Module that returns the dictionary description of an object for JSON."""


def class_to_json(obj):
    """Return the dictionary description of a simple data structure."""
    return obj.__dict__
