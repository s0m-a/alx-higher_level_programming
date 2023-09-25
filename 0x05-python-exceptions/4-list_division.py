#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lists = []
    for x in range(list_length):
        try:
            sol = my_list_1[i] / my_list_2[x]
        except (TypeError, ValueError):
            print("wrong type")
            sol = 0
        except ZeroDivisionError:
            print("division by 0")
            sol = 0
        except IndexError:
            print("out of range")
            sol = 0
        finally:
            lists.append(result)
    return lists
