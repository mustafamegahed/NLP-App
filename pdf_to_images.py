# Convert pdf to images so text can be extractes using ocr

# Import the required packages
from pdf2image import convert_from_path

# Define the path to the PDF file
# For noe we will enter it manually
pdf_path = '/content/file-sample_150kB.pdf'

# Convert the PDF to a JPG image
pages = convert_from_path(pdf_path, dpi=300) # add: first_page=1, last_page=1 to control number of pages

# Provide a number for each image name
image_num = 1000    # Starting from 1000 to make the alphabetical sorting work correctly

# Initiate an empty list to store images names
images_names = []

# Safe images and append images names to their list
for page in pages:
	image_path = 'image_' + str(image_num) + '.jpg'
	page.save(image_path, 'JPEG')
	images_names.append(image_path)
	image_num += 1

# Safe images names to a txt file
with open('images_names.txt', 'w') as file:
    for name in images_names:
        file.write("%s\n" % item)