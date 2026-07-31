#!/usr/bin/python3
"""Module for the Square class."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
