#!/usr/bin/python3
"""A class that defines a square """

class Square:

    def __init__(self,size):
        if (isinstance(size,int)is False):
            raise TypeError("size must be an integer")
        elif size < 0 :
            raise ValueError("size must be >= 0 ")
        else:
            self.__size = size
    """ def area of a square"""
    def area(self):
        return self.__size**2
