def marsExploration(s):
    right = ['S', 'O', 'S']
    n = len(s)
    m = len(right)
    count = 0
    j = 0
    for i in range(n):
        print(s[i], right[j])
        if s[i] != right[j]:
            count += 1
        if j == m - 1:
            j = 0
        else:
            j += 1
    return count


print(marsExploration('SOSSPSSQSSOR'))