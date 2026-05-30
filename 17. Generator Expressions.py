# Similar to list comprehensions but memory efficient (lazy evaluation)
gen = (x**2 for x in range(1, 6))
for val in gen:
    print(val)