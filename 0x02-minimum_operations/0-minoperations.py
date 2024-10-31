#!/usr/bin/python3
"""
Main file for testing
"""

def minOperations(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """


    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        # While `factor` divides `n`, apply the division and count the factor
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
