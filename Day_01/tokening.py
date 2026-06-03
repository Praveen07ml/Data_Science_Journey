

# token size 

words = "This is a string of words".split()

count = len(words)

print(count)


# Getting a response from a API Using Grok Ai service model


from dotenv import load_dotenv
import os

from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    max_tokens = 1000,
    messages=[
        {"role" : "system" , "content" : "You are a helpful assistant that helps me in my AI Leaning Jorney as a strict instructor brutal truth"},
        {"role" : "user" , "content" : "what do you think about 5 years of career break person cna land into AI Engineer work and is it easy to get placed as a fresher and also the present work connecting Groq API to my laptop also done by me i mean the given promt gone throgh hard coding done my self"}

    ]
)

result = response.choices[0].message.content

print(result)