
# Semantic search practice session


from dotenv import load_dotenv
from groq import Groq

import os

#importing embeddding api
from sentence_transformers import SentenceTransformer

#import vector database
import chromadb



load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


#Loadimg Embedding Model

print(f"Loading Embedded Model")

emb_model = SentenceTransformer("all-MiniLM-L6-v2")

print(f"\n Embedded Model Loaded")

# Loading Chroma DB

print(f"\n Vector Database is loaded")

chroma_client = chromadb.Client()

print(f"\n Chroma db locally created")

#Loading Connections like table in Normal data bases

print(f"\n Creating table like collections added to my database")

collections = chroma_client.get_or_create_collection("My_documents")


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


print(f"\n  Adding healthcare Documents to collections")

collections.add(
    documents=healthcare_documents,
    ids=[f"doc {i}" for i in range(len(healthcare_documents))]

)

print(f"\n Uploaded {collections.count()} Documents to collection like table")


def semantic_search(query,n_results=3):

    results = collections.query(
        query_texts=[query],
        n_results=n_results
    )

    return results["documents"][0]


def ask_ai(question,system_prompt="You are Helpful Assistant",max_tokens=250):

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=max_tokens,
            messages=[
                {"role":"system","content":system_prompt},
                {"role":"user","content":question}
            ]
        )

        return response.choices[0].message.content
    
    except Exception as e:
        print(f"\n Error Occured {e}")


def search_and_answer(user_question):

    print(f"\n User Question : {user_question}")

    

    relevant_documents = semantic_search(user_question)

    print(f"\n relavant Documents found")
    print("-"*40)
    

    for i,doc in enumerate(relevant_documents):
        print(f"\n doc{i+1} - {doc}")

    context = "\n".join(relevant_documents)

    prompt = f""" Answer the user question based on the information document provided if the answer is not related to the document
    try to say the user question is not in the current document like words 

    user_question : {user_question}
    
    information_document : {context}

    Answer : """


    result = ask_ai(prompt)
    print(f"\n AI Answer - {result}")
    print("-"*40)

    return result

print(f"="*50)
print(f"\n SEMENTIC SEARCH ENGINE START")
print(F"="*50)

search_and_answer("Tell me about billing problems")
search_and_answer("Tell me what is mechine learning")










    