def calculate_grade(scores):
    """
    Calculate the average score.

    Args:
        scores (list): List of student marks.

    Returns:
        float: Average mark.
    """

    return round(sum(scores) / len(scores), 2)

marks = [85, 90, 78, 88]

print(calculate_grade(marks))

help(calculate_grade)