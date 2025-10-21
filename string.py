s = input("enter a string:")
if len(s) <=1:
   print(s)
else:
   print(s[-1] + s[1:-1] + s[0])
