#!/usr/bin/python3


def canUnlockAll(boxes):
    unlocked = [False] * len(boxes)
    unlocked[0] = True

    s = [0]

    while s:
        curr_box = s.pop()

        for key in boxes[curr_box]:
            if key >= 0 and key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                s.append(key)
