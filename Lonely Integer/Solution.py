def lonelyinteger(a):
    for element in set(a):
        if a.count(element) == 1:
            return element
    return False


print(lonelyinteger([1, 2, 3, 4, 3, 2, 1]))