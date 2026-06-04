

#LLMs does not have memory so the responces may not be relative to questions so thats why chat history stores
# the conversastions and send them back to a new request for each API calling


from dotenv import load_dotenv

import os

from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_messages = []

conversation_messages.append({"role" : "system" , "content" : "yor are Helpful assistent"}) 

conversation_messages.append({"role" : "user" ,"content" : "Hello, How are you and my name is praveen iam 25"})


try:

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=200,
        messages=conversation_messages
    )
except Exception as e:
    print(f"An error occurred: {e}")



ai_reply = response.choices[0].message.content
print(ai_reply)

conversation_messages.append({"role" : "system","content": ai_reply})


conversation_messages.append({"role" : "user" , "content" : "what is my name and age"})

try:

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=20,
        messages=conversation_messages,

    )
    ai_reply = response.choices[0].message.content

except Exception as e:
    print(f"Error occured {e}")

else:
    print(ai_reply)


conversation_messages.append({"role":"system", "content":ai_reply})


