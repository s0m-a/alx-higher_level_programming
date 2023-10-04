def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function will returns None
    """
    if len(list) == 0:
        return None
    res = list[0]
    i = 1
    while i < len(list):
        if list[i] > res:
            res = list[i]
        i = i + 1
    return res
