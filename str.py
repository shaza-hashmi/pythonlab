word = input("enter a string:")

if word[-3:] == "ing":
    word += "ly"
else:
    word += "ing"

print(word)

