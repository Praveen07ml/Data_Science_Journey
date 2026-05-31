
# Dictionary stores data as a key value pairs using keys as a position to retireve value

model_info =  {
    "model" :  "Samsung",
    "provider" : "B new Mobiles",
    "max_price" : 15000

}


print(model_info["model"])

model_info["status"] = "Sold"

print(model_info)


for key,value in model_info.items():
    print(f"key : {key} ,value : {value}")