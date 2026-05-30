sentence = "python programming"
vowels = "aeiou"
count = sum(1 for char in sentence if char.lower() in vowels)
print("Number of vowels:", count)