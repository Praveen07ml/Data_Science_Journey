

# function is a reusable bloack of code that performs a specifictask



def greet(name="user"):

    return f"Welcome {name}"

result = greet("praveen")

print(result)

print(greet())


# multiply two parameters


def product(a,b):
    
    return a * b

result = product(4,5)

print(result)

print(product(10,13))



# creating a prompt


def prompt(answer):

    return f"Answer the following question : {answer}"

result = prompt("So tell me your name?")

print(result)




# check token limit

def token_limit(tokens):

    if tokens > 1200:
        return "Tokens Exceeded"
    
    else:
        return "tokens within limit"
    

result = token_limit(1500)
print(result)



# default model

def model_check(model="gpt-3.5-turbo"):

    return f"Using model : {model}"

result = model_check()
print(result)