#!/usr/bin/python3
def weight_average(my_list=[]):
    _sum = 0
    weight = 0
    if my_list == []:
        return 0
    else:
        for a in my_list:
            _sum = _sum + (a[0] * a[1])
            weight = weight + a[1]
        average = _sum / weight
        return average
