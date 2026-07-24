import pandas as pd

students = pd.read_csv("read_a_csv_file.csv")

print(students.head())

students.info()