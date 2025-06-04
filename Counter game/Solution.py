#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#
import math


def counterGame(n):
    players = ['Louise', 'Richard']
    while n > 1:
        n -= pow(2, math.floor(math.log2(n - 1)))
        if n <= 1:
            return players[0]
        players = players[::-1]
    return players[0]


#print(counterGame(1533726144))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
