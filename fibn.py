def f(n):return n if n < 2 else f(n - 1) + f(n - 2)
for i in range(int(input("terms:"))):
    print(f(i) , end = ' ')
