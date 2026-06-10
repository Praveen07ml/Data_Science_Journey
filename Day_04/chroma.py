

# Chroma DB its a database to store document emebedings when user asks a question the embedings used to 
# search for stored embeddings and return documents chunks relatedto user question embeddings


import chromadb

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


# creating a client to runs locally on my computer 

client = chromadb.Client()

# create collection like normal table in normal databases

collection = client.create_collection("My_Documents")

# adding documents

documents = [
    "Patient Rahul missed his cardiology appointment on Monday",
    "The ER wait time was 45 minutes on Friday evening",
    "Doctor Priya specializes in neurology and sees 20 patients daily",
    "Hospital billing showed 30 percent of invoices were unpaid",
    "Patient no show rate increased by 15 percent in December"
]

# adding above docs to collection

collection.add(
    documents=documents,
    ids=[f"doc{i}" for i in range(len(documents))]
)

print(f" added {collection.count()} documents")


# search for similarity

query = "which patients did not come to their appointments"

#search by similarity

result = collection.query(
    query_texts=[query],
    n_results=2
)


print(f"\n User Query {query}")

print(f"\n Top results :")

for doc in result["documents"][0]:
    print(f" - {doc}")


