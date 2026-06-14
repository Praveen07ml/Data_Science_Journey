

# reading files 


def load_document(file_path):

    with open(file_path,"r",encoding="utf-8") as file:
        content = file.read()

    return content


content = load_document("hospital_report.txt")

print(f"The document size : {len(content)} charecters")

print(f"the first 300 charecters : {content[:200]}")
