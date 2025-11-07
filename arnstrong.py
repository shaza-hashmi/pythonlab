def is_armstrong(n):
    return n == sum(int(d)**len(str(n)) for d in str(n))

l, h = int(input("Lower: ")), int(input("Upper: "))
print("Armstrong numbers:", [i for i in range(l, h+1) if is_armstrong(i)])

