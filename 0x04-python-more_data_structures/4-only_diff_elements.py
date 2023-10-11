#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    def exists_not(my_set, x):
        for a in my_set:
            if a == x:
                return False
        return True

    diff_1 = list(filter(lambda a: exists_not(set_1, a), set_2))
    diff_2 = list(filter(lambda a: exists_not(set_2, a), set_1))
    return (diff_1 + diff_2)
