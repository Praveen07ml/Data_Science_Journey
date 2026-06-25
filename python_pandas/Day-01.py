
import pandas as pd

data = {
    "name": ["Rahul", "Priya", "Arjun"],
    "city": ["Hyderabad", "Mumbai", "Delhi"],
    "age": [25, 28, 22]
}

df = pd.DataFrame(data)

print(df)
print()

# Selecting one column

print(df["name"])
print()

# Reading Shape

print(df.shape) # this gives me the number of rows and columns
print()


# Readin Top rows

print(df.head(2)) #it gives top few rows the number represented in braackets tells me how many you want
print()

# Reading Bottom rows  
print(df.tail(2))  # mirror to head
print()



# Adding a new column

df['applied_dates'] = ["2025-05-01","2025-05-09","2026-05-01"]   #i can add anew column to an existing table just by giving name and list of values same as row numbers of that table

print(df)
print()  


data = {
    'customer_name': ['Rahul', 'Priya', 'Arjun', 'Sneha', 'Vikram'],
    'city': ['Hyderabad', 'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad'],
    'amount': [45000, 25000, 8000, 5000, 45000],
    'product': ['Laptop', 'Phone', 'Desk', 'Chair', 'Laptop']
}


df = pd.DataFrame(data)

print(df)
print()

# Filtering Rows

result = df['amount'] > 20000
print(df[result])
print()


print(df[df["city"]=="Hyderabad"])
print()

print(df[(df["city"]=="Hyderabad") & (df['amount'] > 2000)])
print()



#sorting_values

high_low = df.sort_values('amount',ascending=False)
print(high_low)
print()


low_high = df.sort_values("amount",ascending=True)
print(low_high)
print()

# Selecting multiple columns

print(df[["customer_name","city","amount"]].sort_values("amount",ascending=False))

