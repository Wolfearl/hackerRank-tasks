#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    if n == 0:
        return 1
    count_of_zeros = bin(n).count('0') - 1
    return 2 ** count_of_zeros


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
