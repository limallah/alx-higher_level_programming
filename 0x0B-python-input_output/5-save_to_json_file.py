#!/usr/bin/python3
"""Save object to a file module"""

import json
import os


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj: object to be serialized.
        filename (str): name of file where string is stored.
    """
    with open(filename, mode='w') as json_file:
        return json.dump(my_obj, json_file)
