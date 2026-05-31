n = 36
divisors = [i for i in range(1, n + 1) if n % i == 0]
print(f"Divisors of {n}:", divisors)