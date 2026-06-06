
# AI Api calling using Groq Client Library


from dotenv import load_dotenv
import os

from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

try :

    def api_calling(question,system_prompt="You are a Helpful assistant",max_tokens=200):

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens = max_tokens,

            messages=[
                {"role": "system" , "content" : system_prompt},
                {"role": "user" , "content" : question}

            ]
        )
        return response.choices[0].message.content
    
except Exception as e:

    print(f"Error Occured : {e}")


print(api_calling("What is the capital of india?"))

print("-----------------------------")


print(api_calling("what is the best thing do i need to do for my future in AI feild"))
