#!/usr/bin/python3
"""
print the first and last name
"""

def say_my_name(first_name, last_name=""):
    """ prints "My name is" follewd by the first name and optional last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("my name is", fist_name, last_name)
