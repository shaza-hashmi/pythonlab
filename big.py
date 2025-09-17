a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))
if a>=b and a>=c:
   biggest = a
elif b>=a and b>=c:
   biggest = b
else:
   biggest = c
print("The biggest number is :",biggest)


