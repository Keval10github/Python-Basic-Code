# Safely opening and closing a file using 'with'
with open("sample.txt", "w") as file:
    file.write("Hello, Context Manager!")
print("File written and closed safely.")