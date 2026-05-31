import string
text = "Hello, World! How's it going?"
clean_text = "".join(char for char in text if char not in string.punctuation)
print("Cleaned text:", clean_text)