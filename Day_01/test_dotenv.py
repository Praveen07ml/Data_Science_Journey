

from dotenv import load_dotenv

import os


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
manager_name = os.getenv("MANAGER_NAME")

print(f"API key : {api_key[:10]}")
print(f"Manager name : {manager_name}")