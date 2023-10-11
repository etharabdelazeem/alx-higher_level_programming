#!/usr/bin/python3
def roman_to_int(roman_string):
    int_sum = 0
    letter = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None:
        return 0
    else:
        for i in range(len(roman_string)):
            if (roman_string[i] not in list(letter)):
                return 0
            elif i + 1 < len(roman_string) and letter[roman_string[i+1]]\
                    > letter[roman_string[i]]:
                int_sum = int_sum - letter[roman_string[i]]
            else:
                int_sum = int_sum + letter[roman_string[i]]
        return int_sum
