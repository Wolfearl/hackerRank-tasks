#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

import heapq as hq


def cookies(k, A):
    count = 0
    q = []
    for elm in A:
        hq.heappush(q, elm)
    while any(k > elm for elm in q) and len(q) > 1:
        hq.heappush(q, hq.heappop(q) + 2 * hq.heappop(q))
        count += 1
    if all(k <= elm for elm in q):
        return count
    return -1


print(cookies(7, [1, 2, 3, 9, 10, 12]))
