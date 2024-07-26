import os
from docx import Document

# Path to the directory containing the offer files
oferte_test_path = 'Oferte test'  # Update with your directory path

# Function to extract text from a single document
def extract_text_from_docx(file_path):
    document = Document(file_path)
    doc_text = []
    for paragraph in document.paragraphs:
        doc_text.append(paragraph.text)
    return '\n'.join(doc_text)

# List to store text from all documents
all_docs_text = []

# Iterate over all .docx files in the specified directory
for filename in os.listdir(oferte_test_path):
    if filename.endswith('.docx'):
        file_path = os.path.join(oferte_test_path, filename)
        doc_text = extract_text_from_docx(file_path)
        all_docs_text.append(doc_text)

# Print or do something with the extracted text from all documents
for i, doc_text in enumerate(all_docs_text):
    print(f"Document {i+1}:\n{doc_text}\n")
