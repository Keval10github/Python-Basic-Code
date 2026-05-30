# A function that calls itself
def countdown(n):
    if n <= 0:
        print("Liftoff!")
    else:
        print(n)
        countdown(n - 1)

countdown(3)