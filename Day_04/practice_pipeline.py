

from dotenv import load_dotenv
from groq import Groq
import os
import pandas as pd


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_ai(question,system_prompt="You are helpful assistant",max_tokens=200):

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=max_tokens,
            messages=[
                {"role": "system","content": system_prompt},
                {"role" : "user" , "content": question}

            ]

        )
        return response.choices[0].message.content
    
    except  Exception as e:
        print(f"Error detected {e}")


def classify_customer(row):

    prompt = f"""A customer has these details:
              Age: {row['age']}
              City: {row['city']}
              Purchase Amount: {row['purchase']}
              

Classify this customer as exactly one of these: High,Medium,Low Values
Reply with only the label. Nothing else."""
    
    return ask_ai(prompt,system_prompt="You are Helpful classifier and reply with label")

    r

# Loading Data

print("Loading Data")
print("-"*40)

df = pd.read_csv("customers_clean.csv")

print(df.head())


# cleaning data

print("Cleaning Data")
print("-"*40)

print(df.isnull().sum())


df = df.fillna({
    "name" : "Unknown",
    "age" : df["age"].mean(),
    "city" : "Unknown",
    "purchase" : 0
})

print("After Cleaning")
print("-"*40)
print(df.isnull().sum())

print()
print(df.head())
print(df.tail())


# Applying

print("Ai Labelling")
print("-"*40)

df['ai_label'] = df.apply(classify_customer,axis=1)

print("Labellling Completed")
print("-"*40)

print(df)
print()

# Analyzing Results

print("Analysing Results")
print("-"*40)

print(df.groupby("city")['ai_label'].count().sort_values(ascending=False))
print()
print(df.groupby('ai_label')['purchase'].mean().sort_values(ascending=False))
print()
print(df.groupby('ai_label').size())
print()


#Saving Dataframe into Csv

print("Saving Dataframe into CSV")
print("-"*40)

df.to_csv("processed_customers.csv",index=False)
print(f"saved file into processed_customers.csv")

# summary

print("Summary")
print("-"*40)

print(f"Total Processed Rows {len(df)}")

print(f"High Value : {len(df[df['ai_label']=='High'])}")
print(f"Medium Value : {len(df[df['ai_label']=='Medium'])}")
print(f"Low Value : {len(df[df['ai_label']=='Low'])}")

print("-"*40)
print("Pipe Line Compelted")