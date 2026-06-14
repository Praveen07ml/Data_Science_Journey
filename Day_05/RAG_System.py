
# Building RAG Chatbot

from dotenv import load_dotenv
from groq import Groq
import os

from sentence_transformers import SentenceTransformer
import chromadb


load_dotenv()
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Loading Embedding Model")
emb_model = SentenceTransformer("all-MiniLM-L6-v2")
print(f"\n Model Loaded")


def load_document(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return content



def chunk_document(text,chunk_size=300,overlap=30):

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(chunk)
        
        start = end - overlap

    return chunks



def Knowledge_base(file_path):

    print(f"\n Loading Document : {file_path}")
    document = load_document(file_path)
    print(f"\n Document Loaded : {len(document)} characters")

    chunks = chunk_document(document)
    print(f"\n Document split into {len(chunks)} chunks ")


    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection("helthcare_rag")

    collection.add(
        documents=chunks,
        ids=[f"chunk{i}" for i in range(len(chunks))]
        
    )

    print(f"Knowledge Base is ready with {collection.count()} chunks")

    return collection 

def semantic_search(collection,question,n_results=3):

    results = collection.query(
        query_texts = [question],
        n_results = n_results
    )

    return results["documents"][0]


def ask_ai(prompt,system_prompt, max_tokens=500):

    try:
        response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=max_tokens,
        messages=[
            {"role" : "system", "content" : system_prompt},
            {"role" : "user" , "content" : prompt}
        ])

        return response.choices[0].message.content
    
    except Exception as e:
        print(f"\nError Occured {e}")


def rag_answer(collection,user_question):

    relavant_chunks = semantic_search(collection,user_question)

    context = "\n".join(relavant_chunks)

    prompt = f"""Answer the question using only the information provided below.
If the answer is not in the information say:
I do not have that information in the provided documents.
Do not make up any numbers or facts.

Information:
{context}

Question: {user_question}

Answer:"""

    system_prompt = """You are a healthcare data analyst assistant.
Answer only from the provided context.
Be specific with numbers when they are available.
Never guess or make up information."""

    answer = ask_ai(prompt,system_prompt)

    return answer,relavant_chunks


def main():

    collection = Knowledge_base("hospital_report.txt")

    print(f"\n {"="*80}")
    print("HEALTHCARE RAG CHATBOT")
    print("Ask the questions about the hospital report")
    print("Type 'exit' to quite")
    print("="*80)

    while True:

        print()
        user_question = input("Your_Question : ").strip()

        if user_question.lower() == 'exit':
            print("Good Bye")
            break

        if not user_question:
            print("Please Type Question")
            continue

        print(f"\n Searching for knowledge base...")

        answer,sources = rag_answer(collection,user_question)

        print(f"\nAnswer: {answer}")
        print(f"\nSources used:")
        for i, source in enumerate(sources):
            print(f"{i+1}. {source[:100]}...")
        print("-" * 60)


if __name__ == "__main__":
    main()






