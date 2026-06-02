# write a basic f-string using your name age and city

name = "praveen"
age = 25
city = "Hyderabad"

prompt = f"My name is {name} and i am {age} years old,i live in {city}"

print(prompt)



# build a multi-line prompt using two variables — document and question

document = "The Capital of India is New Delhi"

question = "What is the capital of india?"

promt = f""" Document : {document}

Question : {question}"""

print(promt)



# write a function called build_prompt(topic, level) that returns a multi-line f-string prompt — call it 3 times with different values

def build_prompts(topic,level):

    promt = f""" Topic : {topic}
Level : {level}"""  
    
    return promt

print(build_prompts("Python","Beginner"))


print(build_prompts("Excel","Advanced"))

print(build_prompts("SQL","Intermediate"))


