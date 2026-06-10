

# Building a sementics search engine


from dotenv import load_dotenv
from groq import Groq

import os

from sentence_transformers import SentenceTransformer
import chromadb

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Loading Embedded Model

print("\nLoading Embedded Model")

emb_model = SentenceTransformer("all-MiniLM-L6-v2")

print("\n Model Loaded")

# Using Chroma DB

chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection("Healthcare_Documents")

# healthcare documents 

healthcare_documents = [
    "Patient no show rate in cardiology department increased by 20 percent in Q4",
    "ER average wait time was 52 minutes during peak hours on weekends",
    "Doctor Sharma sees maximum patients in orthopedics department",
    "Hospital billing department reported 35 percent unpaid invoices in November",
    "Patient readmission rate reduced after implementing discharge follow up calls",
    "Neurology department has longest average wait time of 67 minutes",
    "Female patients aged 30 to 50 have highest appointment compliance rate",
    "Monday mornings have highest patient volume across all departments",
    "ICU bed occupancy reached 95 percent during winter months",
    "Patients from rural areas have 40 percent higher no show rate than urban patients",
    "Emergency department handled 200 cases per day during festival season",
    "Pediatrics department shows lowest billing disputes among all departments",
    "Senior patients above 60 years require average 3 follow up appointments",
    "Staff shortage in night shifts increased patient wait time by 30 minutes",
    "Digital appointment reminders reduced no show rate by 25 percent"
]


# Adding Documents to collection 

collection.add(
    documents=healthcare_documents,
    ids=[f"doc{i}" for i in range(len(healthcare_documents))]
)

print(f"\n Added {collection.count()}Documents ")


# Building Sementic search

def sementic_search(query,n_results=3):

    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results["documents"][0]


def ask_ai(question,system_prompt="You are Helpful Assistant",max_tokens=500):

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=max_tokens,
            messages=[
                {"role" : "system" , "content" : system_prompt},
                {"role" : "user" , "content": question}
            ]
        )
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error Occured - {e}")


def search_and_answer(user_question):

    print(f"\n User Question : {user_question}")

    relanvant_docs = sementic_search(user_question,n_results=2)

    print(f"\n Relanvant Documents are found : ")
    print("-"*40)

    for i,doc in enumerate(relanvant_docs):
        print(f"{i+1} - {doc}")

    context = "\n".join(relanvant_docs)

    prompt = f""" Answer the question based on the information bellow if the answer is not in
    documented information say you do not have the answer based on document

    document_infomration : {context}
    User question : {user_question}
    Answer : ""
"""
    answer = ask_ai(prompt)
    print(f"\n AI answer -  {answer}")
    print("-"*40)
    return answer



print("="*50)
print(f"\n SEMENTIC SEARCH DEMO")
print()
print("="*50)

search_and_answer("Which department has the worst wait times?")
search_and_answer("What is the no show rate situation?")
search_and_answer("Tell me about billing problems")
search_and_answer("Which patients miss appointments most often?")
search_and_answer("What happens during peak hours?")