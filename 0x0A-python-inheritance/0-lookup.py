#!/usr/bin/python3
"""
0-lookup.py
function that returns the list of available attributes and methods of an object
"""

def lookup(obj):

    """ Returns: a list of availablel attributes and methods of
	an object"""
    return dir(obj)
