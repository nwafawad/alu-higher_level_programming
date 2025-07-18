#!/usr/bin/python3
"""
this module builds Pascal triangle
"""


def pascal_triangle(n):
    """Returns Pascal’s triangle up to n rows"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i - 1]
        current_row = [1]
        for j in range(1, len(prev_row)):
            current_row.append(prev_row[j - 1] + prev_row[j])
        current_row.append(1)
        triangle.append(current_row)
    return triangle
