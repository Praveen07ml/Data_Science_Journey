
# Building a pipeline applying for AI Response

from dotenv import load_dotenv
import os
from groq import Groq
import pandas as pd

load_dotenv()


# connecting qroq client and accessing Groq API 

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(question,system_prompt="You are Helpful Assistant",max_tokens=200):

    try :

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens = max_tokens,
            messages=[
                {"role" : "system","content" : system_prompt},
                {"role" : "user" , "content" : question}
            ]
        )

        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error Occured {e}")


def classify_customers(row):

    prompt = f"""A customer has these details:
              Age: {row['age']}
              City: {row['city']}
              Purchase Amount: {row['purchase_amount']}
              Product Category: {row['product_category']}

Classify this customer as exactly one of these: High,Medium,Low Values
Reply with only the label. Nothing else."""
    
    return ask_ai(prompt,system_prompt="You are Helpful classifier and reply with label")


# Loading Data

print(f"Loading Data")
print()

df = pd.read_csv("customers_details.csv")

print(f"loaded {len(df)} rows")

print(df.head())

print() 

# Cleaning Data

print()

print(f"cleaning Data")

missing_values = df.isnull().sum()
print(f"Total Missing values {missing_values}")
print()

# filling data with appropiate Values

df = df.fillna(
    {
        "age" : df["age"].mean(),
        "purchase_amount" : 0
    }
)

print(f"After filling Data, Missing Values {df.isnull().sum()}")

print()

# classifying each customer using AI

df["ai_label"] = df.apply(classify_customers,axis=1)

print("Classification Complete")

print(df.head())

print()


# Analysing the Results

print("results by city")

print(df.groupby("city")["ai_label"].count())

print()

print("results by product_category")

print(df.groupby("product_category")['ai_label'].count())

print()

print("Results Avg amount by ai label")

print(df.groupby("ai_label")["purchase_amount"].mean().sort_values(ascending=False))
print()


# save the dataframe to csv

df.to_csv("customer_pipline_processed.csv",index=False)
print(f"Save Dataframe into customer pipeline csv file")

print()

# summary 

print("Summary")
print("-"*40)

print(f"Total Customers Processed {len(df)} rows")

print(f" High Value : {len(df[df['ai_label'] == "High"])}")
print(f" Medium Value : {len(df[df['ai_label'] == "Medium"])}")
print(f"Low Value : {len(df[df['ai_label'] == "Low"])}")