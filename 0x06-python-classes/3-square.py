#!/usr/bin/python3
"""Area of a square"""



class Square:
    """Square defined class with private attributes"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0
            raise ValueError ("size must be >= 0")
            else:
                self.__size = size
        elif not isinstance(size, int):
            raise TypeError ("size must be an integer")

    def area(self):
        """Return area of a square"""
        return int(self.__size) * int(self.__size)
