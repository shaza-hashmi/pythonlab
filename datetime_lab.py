from datetime import datetime

now = datetime.now()

print("Date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Week number:", now.strftime("%U"))
print("Week day:", now.strftime("%A"))
print("Day of year:", now.strftime("%j"))
print("Day of month:", now.day)
print("Day of week:", now.isoweekday())


