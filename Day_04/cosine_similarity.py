# cosine similarity is used to measure how to vectors are similar in direction 

# it means like a person going towards 10 m north
# and other person going towards 100m north
# both travelling in different distances but they are going in same directions so they have similar meaning of 1 score


import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def cosine_similarity(vect1,vect2):

    dot_product = np.dot(vect1,vect2)
    magnitudes = np.linalg.norm(vect1) * np.linalg.norm(vect2)

    return dot_product / magnitudes


# sentences 

sentence1 = "Doctor"
sentence2 = "physician"
sentence3 = "cricket"
sentence4 = "kits"
sentence5 = "Medical bills"
sentence6 = "Balls"






emb1 = model.encode(sentence1)
emb2 = model.encode(sentence2)
emb3 = model.encode(sentence3)
emb4 = model.encode(sentence4)
emb5 = model.encode(sentence5)
emb6 = model.encode(sentence6)


score1 = cosine_similarity(emb1,emb2)
score2 = cosine_similarity(emb3,emb4)
score3 = cosine_similarity(emb5,emb6)

max_scores = [score1,score2,score3]

for score in max_scores:
    print(score)