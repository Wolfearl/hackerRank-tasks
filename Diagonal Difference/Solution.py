def diagonalDifference(arr):
    n = len(arr)
    j = n - 1
    sum_one = 0
    sum_two = 0
    for i in range(n):
        sum_one += arr[i][i]
        sum_two += arr[i][j]
        j -= 1
    if sum_two > sum_one:
        return sum_two - sum_one
    else:
        return sum_one - sum_two



print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))