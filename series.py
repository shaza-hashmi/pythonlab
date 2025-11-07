import math

n = int(input("Enter n: "))
print("Sum =", sum((i**3) / math.factorial(i) for i in range(1, n + 1)))


