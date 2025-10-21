tokens = input("Enter key value pairs: ").split()
d = dict(zip(tokens[0::2], tokens[1::2]))
print("Ascending:", dict(sorted(d.items())))
print("Descending:", dict(sorted(d.items(), reverse=True)))



