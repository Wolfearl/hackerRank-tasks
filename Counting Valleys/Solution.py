def countingValleys(steps, path):
    count = 0
    pathi = {'U': 'D', 'D': 'U'}
    q = [path[0]]
    for i in range(1, steps):
        if len(q) > 0:
            if q[0] == 'U':
                itis = 'M'
            else:
                itis = 'V'
            if q[0] == pathi[path[i]]:
                q.pop()
                if not q and itis == 'V':
                    count += 1
            else:
                q.append(path[i])
        else:
            q.append(path[i])
    return count

print(countingValleys(8, 'UDDDUDUU'))