#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_list = set(my_list)
    my_sum = 0
    for a in set_list:
        my_sum = my_sum + a
    return my_sum
