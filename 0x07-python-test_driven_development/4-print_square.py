#!/usr/bin/python3
'''
Module of function `print_square()` that prints a square
Using '#' character
'''


def print_square(size):
    '''
    prints a square using # character
    Arguments:
        size: the size of the square
    '''
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print(''.join(['#' for c in range(size)]))
