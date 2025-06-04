def arrayManipulation(n, queries):
    diff = [0] * (n + 2)

    for i, j, element in queries:
        diff[i] += element
        diff[j + 1] -= element

    max_num = 0
    curr_sum = 0
    for i in range(1, n + 1):
        curr_sum += diff[i]
        max_num = max(max_num, curr_sum)

    return max_num


print(arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))