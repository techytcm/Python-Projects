numbers = (
    x ** 2
    for x in range(100000000)
)

for _ in range(5):
    print(next(numbers))