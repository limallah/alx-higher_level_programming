#!/usr/bin/python3
"""Appends to a file"""


def append_write(filename="", text=""):
    """
    A function that writes a string to a text file (UTF8)
    and returns the numbers of characters within
    """
    with open(filename, mode='a', encoding='UTF-8') as my_file:
        return my_file.write(text)
