#!/usr/bin/python3

def canUnlockAll(boxes):
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
