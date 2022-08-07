#!/usr/bin/python3
"""create object from a JSON file"""
import os
import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”"""
    with open(filename, mode='r') as json_file:
        return json.load(json_file)
