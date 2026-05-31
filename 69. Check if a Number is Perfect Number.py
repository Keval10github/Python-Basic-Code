n = 28
sum_divisors = sum([i for i in range(1, n) if n % i == 0])
print(f"Is {n} a perfect number?", sum_divisors == n)