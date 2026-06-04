

# Buiding chatbot from scratch 

from dotenv import load_dotenv
import os

from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_ai(question,conversation_history,max_tokens=100):

    conversation_history.append({
        "role": "user",
        "content": question
    })

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=max_tokens,
            messages=conversation_history
        )

        ai_reply = response.choices[0].message.content

        conversation_history.append({
            "role":"assistant",
            "content": ai_reply
        })

        return ai_reply
    
    except Exception as e:
        return f"Error occured: {e}"
    

def trim_messages(conversation_history,max_messages=10):

    system_message = conversation_history[0]
    recent_messages = conversation_history[-max_messages:]

    return [system_message] + recent_messages

def save_conversation(conversation_history,filename="conversation_history.txt"):

    with open(filename,'w',encoding='utf-8') as file:

        for message in conversation_history:
            file.write(f"{message['role'].upper()} : {message['content']}\n")
            file.write("-" *50 + "\n")

        print(f"conversation history stored : {filename}")



print("AI Chatbot started! if you want to quite type 'exit'")

print("-" * 40)


conversation_history = [
    {
        "role" : "system",
        "content" : "you are a helpful assistant that provides concise and accurate answers to user questions"
    }
]


while True:

    user_input = input("you: ")

    if user_input.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        save_conversation(conversation_history)
        break

    if user_input.strip() == "":
        print("Please enter a valid message.") 
        continue


    reply = ask_ai(user_input,conversation_history)
    print(f"AI : {reply}")

    print()


