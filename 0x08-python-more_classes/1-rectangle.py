#!/usr/bin/python3
'''
This module conatains an implementation of a Rectangle class
'''


class Rectangle:
    '''
    This class defines a rectangle having a width and a
    height
    '''
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''
        returns the value of the width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        sets the value of the rectangle's width
        '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''
        returns the value of the height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        sets the value of the rectangle's height
        '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
