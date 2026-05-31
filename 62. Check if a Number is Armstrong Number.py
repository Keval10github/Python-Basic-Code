num = 153
order = len(str(num))
sum_digits = sum(int(digit)**order for digit in str(num))
print(f"Is {num} an Armstrong number?", num == sum_digits)