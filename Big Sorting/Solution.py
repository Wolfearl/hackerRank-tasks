def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x), x))

print(bigSorting(['31415926535897932384626433832795', '1', '3', '10', '3', '5']))