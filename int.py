def add(* n):" add number"; return sum(n)
nums = map(int,input("enter numbers:").split())
print("sum = ", add(*nums))
