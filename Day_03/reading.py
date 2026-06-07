
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


# select only name and purchase columns

print(df[["name","purchase"]])

print()


#  filter rows where city is Hyderabad AND purchase is above 1000

print(df[(df['city']=="Hyderabad") & (df['purchase'] > 1000)][["customer_id","name","purchase"]])
print()


#  filter rows where age is below 25 OR purchase is above 4000


print(df[(df["age"] < 25) | (df["purchase"] > 4000)][["name","city","age","purchase"]])