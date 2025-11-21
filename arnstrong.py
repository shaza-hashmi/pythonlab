import Arms

a = int(input("Enter start: "))
b = int(input("Enter end: "))

print("Armstrong numbers between", a, "and", b, "are:")
for i in range(a, b+1):
    if Armstrong.check(i):
        print(i)

