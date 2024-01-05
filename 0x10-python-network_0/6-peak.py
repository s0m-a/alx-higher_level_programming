#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    first_l = len(list_of_integers)
    if first_l is 0:
        return None
    peak = binaryS(list_of_integers, 0, first_l - 1)
    return list_of_integers[peak]

def binaryS(x, low, hig):
    if low >= hig:
        return low
    mid = ((hig - low) // 2) + low
    if x[mid] > x[mid + 1]:
        return binaryS(x, low, mid)
    else:
        return binaryS(x, mid + 1, hig)
