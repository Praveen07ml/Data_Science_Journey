






def document_chunking(text,chunk_size=500,overlap=50):

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(chunk)

        start = end - overlap

    return chunks

document = """
Patient appointment management is critical for hospital operations.
No show rates affect hospital revenue significantly. Studies show that
reminder messages reduce no show rates by up to 30 percent. Cardiology
department has the highest no show rate at 25 percent followed by
orthopedics at 20 percent. Patients from rural areas show 40 percent
higher no show rates compared to urban patients. Age group 20 to 35
has the highest no show tendency. Implementing SMS reminders 24 hours
before appointments reduced no shows by 18 percent in Q3. The hospital
lost approximately 15 lakh rupees in Q4 due to unfilled appointment slots.
ER wait times peak between 6 PM and 10 PM on weekdays. Average wait time
is 45 minutes during peak hours and 20 minutes during off peak hours.
Staffing levels directly impact patient satisfaction scores.
""".strip()

chunks = document_chunking(document,chunk_size=50,overlap=10)

print(f"chunks {len(chunks)}")


for i,chunk in enumerate(chunks):

    print(f" Chunk {i+1} \n -- {chunk}")
    print("-"*40)
