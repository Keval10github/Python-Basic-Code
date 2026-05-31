nums = [10, 50, 20, 90, 30]
smallest = nums[0]
for n in nums:
    if n < smallest:
        smallest = n
print("Smallest number is:", smallest)