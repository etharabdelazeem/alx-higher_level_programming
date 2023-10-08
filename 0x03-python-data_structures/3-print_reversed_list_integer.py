#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for a in range(len(my_list)):
        print("{:d}".format(my_list[a]))

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
