#!/usr/bin/python3
"""Module for read file"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding='UTF-8') as my_file:
        read = my_file.read()
        print(read, end='')
