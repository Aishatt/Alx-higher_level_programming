#!/usr/bin/python3
"""A class that defines a Square"""


class Square:
    """Square class initialized with size"""

    def __init__(self, size=0):

        if (isinstance(size,int)is False):
            raise TypeError("size must be an integer")
        elif size < 0 :
            raise ValueError ("size must be >= 0 ")
        else:
            self.__size = size
