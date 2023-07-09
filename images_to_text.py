# Extracting text from multible images using OCR to output a txt file

# Import the required packages
import easyocr
from PIL import Image

# Create an EasyOCR reader object
reader = easyocr.Reader(['en'])

# Storing images paths in a list
# For now I will store them manually
images_paths = []

# Intiate an empty string to store text in
ocr_text = ''

for image_path in images_paths:
	image = Image.open(image_path)

	# Recognize text in the image
	ocr_result = reader.readtext(image)

	# Extract text from ocr_result
	for chunk in ocr_result: 
  		ocr_text = ocr_text + ' ' + chunk[1]

# Open a file for writing
with open('ocr_text.txt', 'w') as text_file:
    # Write the text to the file
    text_file.write(ocr_text)