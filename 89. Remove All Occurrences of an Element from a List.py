nums = [1, 2, 3, 1, 1, 4, 5]
target = 1
nums = [x for x in nums if x != target]
print(f"List after removing {target}:", nums)