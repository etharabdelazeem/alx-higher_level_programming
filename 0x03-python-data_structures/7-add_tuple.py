#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if(tuple_a and tuple_b):
        if (len(tuple_a) < 1):
            sum1 = 0 + int(tuple_b[0])
            sum2 = 0 + int(tuple_b[1])
        elif (len(tuple_a) == 1):
            sum1 = int(tuple_a[0]) + int(tuple_b[0])
            sum2 = 0 + int(tuple_b[1])
        elif (len(tuple_b) < 1):
            sum1 = 0 + int(tuple_a[0])
            sum2 = 0 + int(tuple_a[1])
        elif (len(tuple_b) == 1):
            sum1 = int(tuple_a[0]) + int(tuple_b[0])
            sum2 = 0 + int(tuple_a[1])
        else:
            sum1 = int(tuple_a[0]) + int(tuple_b[0])
            sum2 = int(tuple_a[1]) + int(tuple_b[1])
        tuple_sum = (sum1, sum2)
        return (tuple_sum)
