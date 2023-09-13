#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    d = 0
    for t in my_list:
        average = average + t[0] * t[1]
        d = d + t[1]
    return float(average / d)
