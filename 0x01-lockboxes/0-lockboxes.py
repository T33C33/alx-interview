#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Module: 0-lockboxes

    This module contains a function
    to determine if all boxes can be unlocked.

    Function:
        canUnlockAll(boxes):
            Determines if all boxes can be
            unlocked given a list of boxes,
            each containing keys to other boxes.

            Parameters:
                boxes (list of list of int):
                A list where each element is a
                list of integers representing keys
                to other boxes.

            Returns:
                bool: True if all boxes can
                be unlocked, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        key = keys.pop()  # Get the next key to try
        for new_key in boxes[key]:
            if new_key < n and not opened[new_key]:  # Valid and unopened box
                opened[new_key] = True
                keys.append(new_key)  # Add the key to check for more boxes

    # Check if all boxes have been opened
    return all(opened)
