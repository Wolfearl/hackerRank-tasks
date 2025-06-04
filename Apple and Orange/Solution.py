def countApplesAndOranges(s, t, a, b, apples, oranges):

    count_apples = 0
    count_oranges = 0

    for apple in apples:
        if s <= apple + a <= t:
            count_apples += 1

    for orange in oranges:
        if s <= orange + b <= t:
            count_oranges += 1

    return [count_apples, count_oranges]


print(countApplesAndOranges(2, 3,1, 5, [2], [-2]))