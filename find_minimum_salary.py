import pandas as pd

maximum = 0

reader = pd.read_csv(
    "employees.csv",
    chunksize=1000
)

for chunk in reader:
    maximum = max(
        maximum,
        chunk["Salary"].max()
    )

print(maximum)