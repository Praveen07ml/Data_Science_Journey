
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

#counting city


print(df.groupby('city').count())


#performing aggregation functions


print()

print(df.groupby('city')[['name','age']].agg(["count"]))


# count how many customers are in each city


print()

print(df.groupby("city")['customer_id'].count().sort_values(ascending=False))



# find the average age per city

print()
print(df.groupby("city")["age"].agg(["mean","count"]).sort_values(by="mean",ascending=False))
print()


# find total purchase amount per city and sort from highest to lowest


print(df.groupby('city')['purchase'].agg(["sum","count"]).sort_values(by="sum",ascending=False))
print()



# Applying custom column based on each value by creating a function

def customer_category(purchase):

    if purchase > 1000:
        return "Premium"
    else:
        return "Regular"
    

df["category"] = df['purchase'].apply(customer_category)
print(df)





# Practice 1 — write a function that labels customers as Local if city is Hyderabad else Other — apply it to create a new column

def customer(city):

    if city == "Hyderabad":
        return "Local"
    else:
        return "Other"
    
df['city_category'] = df['city'].apply(customer)

print(df)

print()

# Practice 2 — write a lambda that converts purchase amount to rupees label — below 1000 is Low, 1000 to 3000 is Medium, above 3000 is High

df['rupees_label'] = df['purchase'].apply(lambda x : "High" if x > 3000 else "Medium" if x > 1000 else "Low")

print(df)


# Practice 1 — load customers.csv — add a label column — save to customers_labelled.csv

df.to_csv("customer_labelled.csv",index=False)