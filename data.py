"""Routines associated with the application data.
"""
from typing import TextIO


import json

with open("r", "C:\\Users\\Derina\\Desktop\\project 8\\json\\course.json") as fh:
    data = json.load(fh)

    for i in data:
        print(i)


