#!/usr/bin/python3

"""Method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Check if all boxes can be opened."""
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    keys = [0]
    for i in keys:
        for j in boxes[i]:
            if j not in keys and j != i and j < len(boxes) and j != 0:
                keys.append(j)

    return len(keys) == len(boxes)
