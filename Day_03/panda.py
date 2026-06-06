
import pandas as pd

data = {
    "name": ["Rahul", "Priya", "Anil", "Sneha", "Kiran"],
    "age": [25, 30, 22, 28, 35],
    "city": ["Hyderabad", "Mumbai", "Bangalore", "Hyderabad", "Chennai"],
    "purchase": [1500, 3200, 800, 2100, 4500]
}


df = pd.DataFrame(data)

print(df)

print(df.head())
print()

print(df.tail())
print()

print(df.info())
print()

print(df.describe())


print(df['age'] )
print(df['city'])

df['city']


print(df[['age']])

print()

print(df[['name','age','city']])


print(df[df['age'] > 25])


# selecting one column

print(df['age']) # return a series
print()

print(df[['age']]) # returns a DataFrame


# slecting Multiple Columns

print(df[['name','age','city']])



# filtering a rows based on a condition

print(df[df['age'] > 25])

print()

print(df[df['city']=='Hyderabad'][['name','purchase']])
print()

# filtering rows based on two conditions with AND

print(df[ (df['age'] > 25) & (df['city'] == 'Hyderabad')][['name','purchase']])
