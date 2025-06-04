def lilysHomework(arr):
    def count_swaps(arr):
        n = len(arr)
        index_map = {value: index for index, value in enumerate(arr)}
        swaps = 0
        for i in range(n):
            while arr[i] != sorted_arr[i]:
                swap_index = index_map[sorted_arr[i]]
                arr[i], arr[swap_index] = arr[swap_index], arr[i]
                index_map[arr[swap_index]] = swap_index
                index_map[arr[i]] = i
                swaps += 1
        return swaps

    sorted_arr = sorted(arr)
    asc_swaps = count_swaps(list(arr))
    desc_swaps = count_swaps(list(arr)[::-1])

    return min(asc_swaps, desc_swaps)


print(lilysHomework([3, 4, 2, 5, 1]))