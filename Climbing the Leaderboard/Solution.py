def climbingLeaderboard(ranked, player):
    ranks = sorted(set(ranked), reverse=True)
    results = []
    index = len(ranks) - 1
    for p in player:
        while index >= 0 and p >= ranks[index]:
            index -= 1
        results.append(index + 2)
    return results

print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]))