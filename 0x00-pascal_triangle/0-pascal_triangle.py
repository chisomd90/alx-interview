#!/usr/bin/python3
"""Writing a function for Pascal's Triangle"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    
    Args:
        n (int): Number of rows to generate the triangle.
        
    Returns:
        list: List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

# Test
print(pascal_triangle(5))

