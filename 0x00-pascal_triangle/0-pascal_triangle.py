#!/usr/bin/python3

def pascal_triangle(n):
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
