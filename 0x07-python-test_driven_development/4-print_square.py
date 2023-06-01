#!/usr/bin/python3
"""
File: 4-print_square.py
Desc: This module contains one capability: print_square(size)
Author: Onyejekwe Philip (Donphili)
Date Created: 1 June 2023
"""


def print_square(size):
    """
    This function prints a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
