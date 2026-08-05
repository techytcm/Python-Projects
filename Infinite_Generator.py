def infinite():
    n = 1
    while True:
        yield n
        n += 1

gen = infinite()

for _ in range(5):
    print(next(gen))