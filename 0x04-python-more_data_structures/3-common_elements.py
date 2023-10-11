#!/usr/bin/python3
def common_elements(set_1, set_2):
    def exists(my_set, x):
        for a in my_set:
            if a == x:
                return True
        return False

    common = list(filter(lambda a: exists(set_1, a), set_2))
    return (common)
