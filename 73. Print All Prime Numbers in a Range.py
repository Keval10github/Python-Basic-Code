lower, upper = 10, 20
print(f"Primes between {lower} and {upper}:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")
print()