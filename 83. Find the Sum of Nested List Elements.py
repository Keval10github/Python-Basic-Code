nested_nums = [[1, 2], [3, 4], [5, 6]]
total = sum(item for sublist in nested_nums for item in sublist)
print("Sum of nested elements:", total)