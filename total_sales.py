import pandas as pd

total = 0

reader = pd.read_csv(
    "sales.csv",
    chunksize=1000
)

for chunk in reader:
    total += chunk["Sales"].sum()

print(total)