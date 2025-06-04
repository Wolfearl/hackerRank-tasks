def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        # Берём подмассив длины m
        segment = s[i:i + m]
        if sum(segment) == d:
            count += 1
    return count


print(birthday([1, 2, 1, 3, 2], 3, 2))