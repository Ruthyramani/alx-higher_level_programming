#!/usr/bin/python3
"""model that defines a square """
class Square:
    """a class that signifies a square"""
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError('size must be >= 0')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size 
    
    @property
    def size(self):
        """retrieves the square of the size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError ('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    
    def area(self):
    """ calculate area of the square, returns the square of the size"""

        return (self.__size ** 2)
    def my_print(self)
    
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)

