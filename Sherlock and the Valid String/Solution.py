from collections import Counter


def isValid(s):
    counters = Counter(s)
    t = list(counters.values())
    count = 0
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            continue
        else:
            t[i + 1] -= 1
            if t[i + 1] == 0:
                t[i + 1] = t[i]
            if t[i] == t[i + 1]:
                count += 1
                continue
            else:
                return "NO"
    if count > 1:
        return "NO"
    return "YES"


print(isValid("aabbc"))