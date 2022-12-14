#!/usr/bin/python3
"""Module of elaborated class Square"""


class Square:
    """Square defined class with private attribute size"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")


'''
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("must be an int")
        elif isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
'''
