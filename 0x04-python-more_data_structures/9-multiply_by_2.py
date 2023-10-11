#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for a in a_dictionary:
        b_dictionary[a] = a_dictionary[a] * 2
    return b_dictionary
