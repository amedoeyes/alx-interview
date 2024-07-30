#!/usr/bin/python3

"""
Lockboxes
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    unlocked = [0]
    for box in unlocked:
        for key in boxes[box]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    return len(unlocked) == len(boxes)
