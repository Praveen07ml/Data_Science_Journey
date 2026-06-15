

from sentence_transformers import SentenceTransformer

import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

#creatating a local db from croma db

client = chromadb.Client()

# creatinng a collection like table 

collection = client.create_collection("my_documents")

#documents



