lower, upper = 100, 500
print(f"Armstrong numbers between {lower} and {upper}:")
for num in range(lower, upper + 1):
    order = len(str(num))
    temp_sum = sum(int(digit)**order for digit in str(num))
    if num == temp_sum:
        print(num, end=" ")
print()