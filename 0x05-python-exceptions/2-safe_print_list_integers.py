#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(0, x):
        try:
            if counter < x:
                print("{:d}".format(my_list[i]), end="")
                counter = counter + 1
        except (TypeError, ValueError):
            pass
    print("")
    return counter
