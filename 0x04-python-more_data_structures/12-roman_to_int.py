#!/usr/bin/python3
def roman_to_int(roman_string):
    int_sum = 0
    letter = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        current = letter[roman_string[i]]
        if i + 1 < len(roman_string) and letter[roman_string[i+1]] > current:
            int_sum = int_sum - current
        else:
            int_sum = int_sum + current
    return int_sum
