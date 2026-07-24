import pandas as pd

employees = {
    "ID": [101,102,103],
    "Name": ["John","Emma","David"],
    "Salary": [45000,50000,48000]
}

df = pd.DataFrame(employees)

print(df)

print(df.head())
print(df.info())