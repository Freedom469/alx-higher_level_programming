#!/usr/bin/python3
""" a class Square that defines a square by size"""


class Square:
    """Instantiation with size"""
    def __init__(self, size=0):
        """Private instance attribute: size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
