
# Reading CSV files

import pandas as pd

df = pd.read_csv("customers.csv")

print(df)


print(df.head())
print()
print(df.tail())
print()
print(df.shape)
print()
print(df.columns)

print()

print(df.info())
print()
print(df.describe()[['age','purchase']])