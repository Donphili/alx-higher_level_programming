#!/usr/bin/python3
"""
File: 0-lookup.py
Desc: This module has  one function; lookup(obj)
Author:Onyejekwe Philip (Donphili)
Date Created: 09 jun 2023
"""


def lookup(obj):
    """
    Returns the list of available attributes and
    methods of an object
    """
    return dir(obj)
