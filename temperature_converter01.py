def celsius_to_fahrenheit(celsius, rounded=True):
    result = (celsius * 9 / 5) + 32

    if rounded:
        return round(result, 2)

    return result

print(celsius_to_fahrenheit(37))

print(celsius_to_fahrenheit(37, False))