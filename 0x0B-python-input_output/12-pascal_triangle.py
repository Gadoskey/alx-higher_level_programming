#!/usr/bin/python3
# Author -- Gadoskey
"""This module defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n"""
    if n <= 0:
        return []

    new_list = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(new_list[i-1][j-1] + new_list[i-1][j])
        new_list.append(row)
    return (new_list)
