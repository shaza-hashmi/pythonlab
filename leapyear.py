import calendar
y = int(input("enter year:"))
if calendar.isleap(y):
    print("leap year")
else:
    print("not a leap year")

