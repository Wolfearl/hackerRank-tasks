def pageCount(n, p):
    gr = [[1]]
    for i in range(2, n + 1, 2):
        if i + 1 != n + 1:
            gr.append([i, i+1])
        else:
            gr.append([i])
    count = 0
    if p > n // 2:
        i = len(gr) - 1
        while p not in gr[i]:
            count += 1
            i -= 1
    else:
        i = 0
        while p not in gr[i]:
            count += 1
            i += 1
    return count

print(pageCount(5, 3))