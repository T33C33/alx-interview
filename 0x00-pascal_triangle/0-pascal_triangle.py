#!/usr/bin/python3
"""
This module provides a function to generate Pascal's triangle.

Pascal's triangle is a triangular array of the binomial coefficients. 
Each row represents the coefficients in the expansion of a binomial raised to successive powers.

Functions:
    pascal_triangle(n): Generates Pascal's triangle up to the nth row.
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    Args:
        n (int): The number of rows of Pascal's triangle to generate.
    Returns:
        List[List[int]]: A list of lists representing Pascal's triangle.
    """
    
    # edge case
    if n <= 0:
        return []

    # Initializing Pascal's triangle list with the first row [1]
    triangle = [[1]]

    # Generating rows of the triangle
    for i in range(1, n):
        # Previous row is the last row in triangle
        prev_row = triangle[-1]
        # Start the new row with [1]
        new_row = [1]

        # Add the middle values
        # Each element is the sum of the two elements directly above it
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        # End the new row with [1]
        new_row.append(1)

        # Add the newly constructed row to the triangle
        triangle.append(new_row)

    return triangle
