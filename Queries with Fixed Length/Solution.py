def solve(arr, queries):
    n = len(arr)
    result = []
    for k in queries:
        maxes = []
        was_first = False
        for i in range(n - k + 1):
            if i == 0 or was_first == True:
                maxes.append(max(arr[i:i + k]))
            else:
                maxes.append(max(maxes[-1], arr[i + k - 1]))

            if maxes[-1] == arr[i]:
                was_first = True
            else:
                was_first = False
        result.append(min(maxes))
    return result


print(solve([33, 11, 44, 11, 55], [1, 2, 3, 4, 5]))