# Install Required packages
# !pip install PyPDF2

# import required packages

import PyPDF2

path = 'file-sample_150kB.pdf'
with open(path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
print(text)
