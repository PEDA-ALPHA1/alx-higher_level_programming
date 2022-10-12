#!/usr/bin/python3
"""Area of a square"""


class Square:
    """Square defined class with private sttribute size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
                raise TypeError("must be an int")
        elif isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
