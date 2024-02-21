#!/usr/bin/python3
# Author -- Gadoskey
"""This module defines a file that reads a file"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
