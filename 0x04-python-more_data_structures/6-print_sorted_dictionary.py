#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    d = sorted(a_dictionary)
    for i in d:
        print("{:s}:".format(i), a_dictionary[i])
