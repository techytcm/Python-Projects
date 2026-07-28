def average(numbers):
    """
    Calculate the average of a list.

    Args:
        numbers (list): List of numeric values.

    Returns:
        float: Average of the list.
    """

    return sum(numbers) / len(numbers)

print(average([10, 20, 30]))