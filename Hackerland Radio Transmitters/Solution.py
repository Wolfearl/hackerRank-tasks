def hackerlandRadioTransmitters(x, k):
    x.sort()
    count = 0
    i = 0
    while i < len(x):
        count += 1
        loc = x[i] + k
        while i < len(x) and x[i] <= loc:
            i += 1
        loc = x[i-1] + k
        while i < len(x) and x[i] <= loc:
            i += 1
    return count


print(hackerlandRadioTransmitters([7, 2, 4, 6, 5, 9, 12, 11], 2))
print(hackerlandRadioTransmitters([1, 2, 3, 4, 5], 1))