# Extracting text from a web page using BeautifulSoup to output a txt file

# Import the required packages
from bs4 import BeautifulSoup
import requests

# Get the website url from user
url = 'https://example.com'

# request the web page
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Use BeautifulSoup to scrape the paragraphs of the page
# Using paragraphs ignores some iformation but returns more clean text
paragraphs = soup.find_all('p')

with open('web_page_text.txt', 'w') as text_file:

	for paragraph in paragraphs:
		# Write the text to the file
		text_file.write(paragraph.text)