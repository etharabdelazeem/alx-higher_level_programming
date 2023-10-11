#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rep_list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            rep_list[i] = replace
    return rep_list
