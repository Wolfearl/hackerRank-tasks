#!/bin/python3
#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    max_here = max_so_far = arr[0]
    max_subsequence = arr[0] if arr[0] > 0 else 0
    for num in arr[1:]:
        max_here = max(num, max_here + num)
        max_so_far = max(max_so_far, max_here)
        if num > 0:
            max_subsequence += num
    if max_subsequence == 0:
        max_subsequence = max(arr)

    return [max_so_far, max_subsequence]

print(maxSubarray([2, -1, 2, 3, 4, -5]))
