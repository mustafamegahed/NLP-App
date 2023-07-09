# Get text directly from the user

user_input_text = input("Enter some text: ")

# Open a file for writing
with open('user_input_text.txt', 'w') as text_file:
    # Write the text to the file
    text_file.write(user_input_text)