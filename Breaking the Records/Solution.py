def breakingRecords(scores):
    min_score = 0
    max_score = 0
    min_scores = scores[0]
    max_scores = scores[0]
    for score in scores[1:]:
        if score < min_scores:
            min_scores = score
            min_score += 1
        elif score > max_scores:
            max_scores = score
            max_score += 1
    return [max_score, min_score]


print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))

