#!/usr/bin/python3
def magic_calculation(a, b):
    sol = 0

    for x in range(1, 3):
        try:
            if (x > a):
                raise Exception('Too far')
            else:
                sol += a ** b / x
        except:
            sol = a + b
            pass
    return (sol)
