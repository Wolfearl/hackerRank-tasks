import heapq


data = []
rem = []
for _ in range(int(input())):
    z = list(map(int, input().split()))
    match z[0]:
        case 1:
            heapq.heappush(data, z[1])
        case 2:
            heapq.heappush(rem, z[1])
        case 3:
            while rem and rem[0] == data[0]:
                heapq.heappop(data)
                heapq.heappop(rem)
            print(data[0])