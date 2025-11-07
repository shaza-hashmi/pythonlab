from datetime import datetime, timedelta

user_input = input("Enter a date (YYYY-MM-DD): ")
today = datetime.strptime(user_input, "%Y-%m-%d").date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

