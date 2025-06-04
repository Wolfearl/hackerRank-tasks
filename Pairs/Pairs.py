#!/bin/python3

import os


def pairs(k, arr):
    d = {}
    result = 0
    for elm in arr:
        d[elm] = 1
        if elm + k in d.keys():
            result += 1
        if elm - k in d.keys():
            result += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
