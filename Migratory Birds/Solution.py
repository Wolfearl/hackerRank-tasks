from collections import Counter


def migratoryBirds(arr):
    counter = Counter(arr)
    result = arr[0]
    max_count = 0
    for key, value in counter.items():
        if value > max_count:
            result = key
            max_count = value
        elif value == max_count:
            if key < result:
                result = key
    return result


print(migratoryBirds([1, 4, 4, 4, 5, 3]))