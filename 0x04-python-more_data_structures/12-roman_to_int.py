#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        rsum = 0
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(roman_string)):

            if i == len(roman_string) - 1:
                rsum += num[roman_string[i]]

            elif num[roman_string[i + 1]] <= num[roman_string[i]]:
                rsum += num[roman_string[i]]

            else:
                rsum -= num[roman_string[i]]

        return (rsum)
    else:
        return (0)
