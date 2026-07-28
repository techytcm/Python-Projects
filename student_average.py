def average(scores, rounded=True):
    avg = sum(scores) / len(scores)

    if rounded:
        return round(avg, 2)

    return avg

marks = [82, 76, 91, 88]

print(average(marks))

print(average(marks, rounded=False))