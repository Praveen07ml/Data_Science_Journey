

import pandas as pd



df = pd.read_csv("customers_missing_values.csv")


print(df.isnull())

print()

print(df.isnull().sum())

print(df[df.isnull().any(axis=1)])


df['name'] = df['name'].fillna("unknown")

print(df[['name']])


df = df.fillna({
    "name" : "unknown",
    "age" : df['age'].mean(),
    "city" : "unkown",
    "purchase": 0
})

print(df)


print(df.groupby('city')["purchase"].agg(['count','sum','mean']))


def label_purchase(amount):

    if amount > 2000:
        return "High Value"
    else:
        return "Low Value"



print()   

df['purchase_group'] = df['purchase'].apply(label_purchase)

print(df)

df['label'] = "processed"


df.to_csv("customers_processed.csv",index=False)

