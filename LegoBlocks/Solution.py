#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def legoBlocks(n, m):
    mod = (10 ** 9 + 7)
    row_comb = [1, 1, 2, 4]
    while len(row_comb) <= m:
        t = row_comb[-4:]
        row_comb.append(sum(row_comb[-4:]) % mod)
    total = [pow(c, n, mod) for c in row_comb]
    unstable = [0, 0]
    for i in range(2, m + 1):
        unstable.append(sum(map(lambda j: (total[j] - unstable[j]) * total[i - j], range(1, i))) % mod)
    return (total[m] - unstable[m]) % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        result = legoBlocks(n, m)
        fptr.write(str(result) + '\n')
    fptr.close()
