#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

from collections import deque


def minimumMoves(grid, startX, startY, goalX, goalY):
    queue = deque([(startX, startY, 0)])
    visited = {startX, startY}
    actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == (goalX, goalY):
            return dist
        for dx, dy in actions:
            nx = x
            ny = y
            while 0 <= nx + dx < n and 0 <= ny + dy < n and grid[nx + dx][ny + dy] == '.':
                nx += dx
                ny += dy
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
    return -1


if __name__ == '__main__':
    n = 3
    grid = ['.X.', '.X.', '...']
    startX = 0
    startY = 0
    goalX = 0
    goalY = 2
    result = minimumMoves(grid, startX, startY, goalX, goalY)
    print(result)
