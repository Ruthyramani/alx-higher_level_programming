#!/usr/bin/python3

for ch in range(ord('a'), ord('z') + 1):
    if chr(ch) != 'e' and chr(ch) != 'q':
        print("{:c}".format(ch), end="")
