

# while true loop kepp running the chat bot so it can take multiple user messages under one session
#without it chat bot runs once and then stops


count = 0 

while True:

    user_input = input("Type your messsage or quite type 'exit' :",)
    count += 1

    if user_input.lower() == "exit":
        print("Exiting the chatbot.Goodbye!")
        break
    
    print(f"you said : {user_input}")


print("total messages sent by user: ",count)





