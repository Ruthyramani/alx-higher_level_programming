#!/usr/bin/python3
'''
    print the last name passed

'''


def say_my_name(first_name, last_name=''):
    '''
    Prints "My name is ..." followed by the full name
    passed as argument
    '''
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    full_name = first_name + ' ' + last_name
    print(f'My name is {full_name}')
