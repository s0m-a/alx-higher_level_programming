#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for ele in set(my_list):
        sum = sum + ele
    return sum
