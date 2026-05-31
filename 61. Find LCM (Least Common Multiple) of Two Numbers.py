import math
a, b = 15, 20
lcm = abs(a * b) // math.gcd(a, b)
print(f"LCM of {a} and {b} is:", lcm)