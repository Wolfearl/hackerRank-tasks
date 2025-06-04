def truckTour(petrolpumps):
    current_petrol = 0
    start = 0
    index = 0
    while start < len(petrolpumps):
        current_petrol += petrolpumps[index][0] - petrolpumps[index][1]
        if current_petrol >= 0:
            index += 1
            if index > len(petrolpumps) - 1:
                index = 0
            if index == start:
                return start
        else:
            start += 1
            index = start
            current_petrol = 0

print(truckTour([[1, 5], [10, 3], [3, 4]]))