#!/usr/bin/python3
"""Module that defines the Pascal's Triangle function"""


def pascal_triangle(n):
    """Repre Pascal's Triangle of x(size)
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tr = triangles[-1]
        tm = [1]
        for i in range(len(tr) - 1):
            tm.append(tr[i] + tr[i + 1])
        tm.append(1)
        triangles.append(tm)
    return triangles
