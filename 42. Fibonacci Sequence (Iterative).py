n_terms = 5
a, b = 0, 1
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b