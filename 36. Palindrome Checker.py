# Checks if a word is the same forwards and backwards
word = "radar"
is_palindrome = word == word[::-1]
print(f"Is '{word}' a palindrome?", is_palindrome)