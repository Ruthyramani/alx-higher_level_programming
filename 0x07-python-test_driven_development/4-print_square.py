#!/bin/usr/python3

"""
this module supplies a functiom 
"""

def print_square(size):
    """ print a square with with the hashtags "#", that has the length of size """
    if type(size) is not int:
        raise TypeError("Size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")

