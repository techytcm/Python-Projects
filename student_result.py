students = [
    "Alice",
    "Bob",
    "Charlie"
]

marks = [
    95,
    88,
    90
]

for s,m in zip(students,marks):
    print(f"{s}: {m}")