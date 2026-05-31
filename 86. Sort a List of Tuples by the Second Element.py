data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
data.sort(key=lambda x: x[1])
print("Sorted by second element:", data)