#!/usr/bin/python3
def uppercase(str):
    STR = ""
    for c in str:
        if (ord(c) >= 97) & (ord(c) <= 122):
            STR = STR+chr(ord(c)-32)
        else:
            STR = STR+c
    print("{}".format(STR))
