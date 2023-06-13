#!/usr/bin/python3
"""
Desc: This module has one function; from_json_string(my_str)
"""

import json


def from_json_string(my_str):
    """
    eturns an object (Python data structure) represented by a
    JSON string
    """
    return json.loads(my_str)
