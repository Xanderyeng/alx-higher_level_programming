#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        print(uppercase_char, end="")
    print()
