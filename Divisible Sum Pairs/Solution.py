def divisibleSumPairs(n, k, ar):
    count  = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                if (ar[i] + ar[j]) % k == 0:
                    count += 1
    return count


print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))