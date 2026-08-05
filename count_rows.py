import pandas as pd

count = 0

reader = pd.read_csv(
    "sales.csv",
    chunksize=1000
)

for chunk in reader:
    count += len(chunk)

print(count)