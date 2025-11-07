def compare(s1, s2, n):
    print("Same" if s1[:n] == s2[:n] else "Different")

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter n: "))

compare(s1, s2, n)


