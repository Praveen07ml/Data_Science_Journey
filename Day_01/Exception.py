# write try/except for division by zero from memory


num1 = 15
num2 = 0
try :

    result = num1/num2

except ZeroDivisionError:

    print("You cannot divide by zero")

else:
    print(f"The result is {result}")



# write a function safe_divide(a, b) that returns 0 if it fails


def division(a,b):
    try :
        result = a/b

    except Exception as e:
        print(f"Something Went wrong : {e}")

        return f"Result is : 0"

    
    else:
        print(f"The result is :{result}")


print(division(10,5))
print(division(10,0))   


