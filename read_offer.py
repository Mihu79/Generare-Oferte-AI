import os
from docx import Document

# Path to one of the offer files
file_path = os.path.join(oferte_test_path, 'Oferta - Test 1.docx') # type: ignore

# Load the document
document = Document(file_path)

# Extract text from the document
doc_text = []
for paragraph in document.paragraphs:
    doc_text.append(paragraph.text)

doc_text
