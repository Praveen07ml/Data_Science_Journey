
# Generating Embeddings

from dotenv import load_dotenv
from groq import Groq

import numpy as np
import os


# Groq does not have embedding API so we use sentence transformers

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentence1 = "The Patient did not show up for the appointment"
sentence2 = "car"
sentence3 = "Dog"
sentence4 = "puppy"
sentence5 = "Honda"


embeddings = model.encode([sentence3,sentence4])

print(f"type - {type(embeddings)}")
print(f"Shape {embeddings.shape}")

for embedding in embeddings:
    print(embedding[:10])



