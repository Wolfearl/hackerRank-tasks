def equalStacks(h1, h2, h3):
    sh1 = sum(h1)
    sh2 = sum(h2)
    sh3 = sum(h3)
    i, j, k = 0, 0, 0
    while sh1 != sh2 or sh2 != sh3:
        m = max(sh1, sh2, sh3)
        if m == sh1:
            sh1 -= h1[i]
            i += 1
        elif m == sh2:
            sh2 -= h2[j]
            j += 1
        else:
            sh3 -= h3[k]
            k += 1
    return sh1


print(equalStacks([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]))