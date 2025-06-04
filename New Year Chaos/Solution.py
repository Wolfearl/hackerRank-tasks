def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)


minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
#              1, 2, 3, 4, 5, 6, 7, 8
