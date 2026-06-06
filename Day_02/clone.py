
# Creating a chatbot from scratch 1


from dotenv import load_dotenv
import os

from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def  ask_ai(question,conversation_history,max_tokens=500):

    conversation_history.append({
            "role" : "user",
            "content" : question
        })
        
    

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=max_tokens,
            messages=conversation_history

        )
        ai_reply = response.choices[0].message.content

        conversation_history.append(
            {
                "role" : "assistant",
                "content" : ai_reply
            }
        )

        return ai_reply
    
    except Exception as e:
        print(f"Error Occured {e}")


def trim_messages(conversation_history,max_messages=10):
    system_message = conversation_history[0]
    recent_messages = conversation_history[-max_messages:]

    return [system_message] + recent_messages

def save_conversations(conversation_history,file_name="conversation_history.txt"):

    with open(file_name,"w",encoding="utf-8") as file:
        
        for message in conversation_history:
            file.write(f"{message['role'].upper()} : {message['content']}\n")
            file.write(f"{"-"*50} \n")

        print(f"Conversation History Stored! : {file_name}")


print("AI Chat bot Runs Now if you want to quite please enter 'exit'")

print("*"*50+"\n")

conversation_history = [
    {"role": "system",
     "content" : "You are useful assistent that give me reliable answers and make me happy or sad but brutal answers"}
]
        

while True:

    user_input = input("User: ",)

    if user_input.lower() == 'exit':
        print("Good Bye! See you again")
        print(save_conversations(conversation_history))
        break

    if user_input.strip() == "":
        print('Please enter valid that you want to answer')
        continue

    reply = ask_ai(user_input,conversation_history)

    print(f"AI : {reply}")

    print()



