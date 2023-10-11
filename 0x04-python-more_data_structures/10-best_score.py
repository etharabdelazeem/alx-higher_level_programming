#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    else:
        key = list(a_dictionary)[0]
        best = a_dictionary[key]
        for a in a_dictionary:
            if a_dictionary[a] > best:
                best = a_dictionary[a]
                key = a
        return key
