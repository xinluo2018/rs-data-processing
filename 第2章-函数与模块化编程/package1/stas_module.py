
def mean_scores(scores):
    return sum(scores) / len(scores)
def max_score(scores):
    return max(scores)
def min_score(scores):
    return min(scores)
def median_score(scores):
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
    else:
        return sorted_scores[mid]
