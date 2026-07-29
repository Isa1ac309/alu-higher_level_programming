#!/usr/bin/python3
"""Module for the MyList class."""


class MyList(list):
    """A subclass of list that can print itself sorted."""

    def print_sorted(self):
        """Print the list, sorted (ascending)."""
        print(sorted(self))
