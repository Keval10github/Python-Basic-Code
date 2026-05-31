sentence = "apple banana apple orange banana apple"
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word frequency:", freq)