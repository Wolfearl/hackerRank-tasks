import heapq

def cookies(k, A):
    heapq.heapify(A)
    i = 0
    while any(k > elm for elm in A) and len(A) > 1:
        heapq.heappush(A, heapq.heappop(A) + 2 * heapq.heappop(A))
        i += 1
    if all(k <= elm for elm in A):
        return i
    else:
        return -1


print(cookies(7, [1, 2, 3, 9, 10, 12]))