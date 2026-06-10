

# Practice 1 — add 10 healthcare related sentences to a collection — search with 3 different queries — verify results make sense

import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-miniLM-L6-v2")

# to run locally on chromadb

client = chromadb.Client()


# creating a collection like tabel

collection = client.create_collection("my_documents")

documents = [
    "Patient Rahul missed his cardiology appointment on Monday",
    "The emergency department treated 120 patients last week",
    "Doctor Priya specializes in neurology and sees 20 patients daily",
    "Hospital billing showed 30 percent of invoices were unpaid",
    "Patient no show rate increased by 15 percent in December",
    "Blood test reports are available within forty eight hours",
    "The pharmacy dispensed 500 prescriptions this month",
    "Patients can schedule appointments through the hospital portal",
    "Insurance claims processing takes approximately seven business days",
    "The pediatric department provides vaccination services for children"
]


# adding dcouments to collection

collection.add(
    documents=documents,
    ids=[f"doc{i}" for i in range(len(documents))]
)

print(f"\n {collection.count()} documents loaded")

# search by similarity

query = "How can I book a doctor appointment?"
query1 = "Where do I get my blood report?"
query2 = "Children vaccination services"


result = collection.query(
    query_texts=[query,query1,query2],
    n_results=2
)


for i,docs in enumerate(result["documents"]):

    print(f"\n User Query {i+1}")
    print("-"*40)

    for doc in docs:
        print(f"- {doc}")




