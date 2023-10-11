#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for a in a_dictionary:
        if a_dictionary[a] == value:
            keys.append(a)
    for key in keys:
        del a_dictionary[key]
    return a_dictionary
