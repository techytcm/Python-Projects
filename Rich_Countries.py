countries = [
    "A",
    "B",
    "C"
]

gdp = [
    500,
    1500,
    300
]

rich = [
    country
    for country, value
    in zip(countries, gdp)
    if value > 1000
]

print(rich)