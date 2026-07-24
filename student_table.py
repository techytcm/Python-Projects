import pandas as pd

students = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 22, 21],
    "Department": ["CSE", "SWE", "EEE"]
}

df = pd.DataFrame(students)

print(df)