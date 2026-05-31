scores = {'John': 85, 'Alice': 92, 'Bob': 78}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))
print("Sorted dictionary by value:", sorted_scores)