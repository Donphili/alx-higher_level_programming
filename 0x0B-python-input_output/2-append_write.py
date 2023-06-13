#!/usr/bin/python3
"""
Desc: This module has one function;
append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return f.write(text)
