#!/usr/bin/python3
"""
Desc: This module has one function;
write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        return(f.write(text))
