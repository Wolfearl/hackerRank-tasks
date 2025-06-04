def getTotalX(a, b):
    count = 0
    for i in range(1, max(b) + 1):
        if all(i % el == 0 for el in a) and all(el % i == 0 for el in b):
            count += 1
    return count


print(getTotalX([2, 4], [16, 32, 96]))