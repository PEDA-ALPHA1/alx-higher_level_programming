#!/usr/bin/python3
"""Module of even more evolved Square class"""


class Square:
    """private attribute size"""
    def __init__(self, size=0):

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")

    def area(self):
        """returns current square area"""
        return int(self.__size) * int(self.__size)
