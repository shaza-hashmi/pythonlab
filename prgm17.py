d = eval(input("Enter a dictionary: "))  # e.g. {'b': 2, 'a': 1, 'c': 3}

# Sort by keys
asc = dict(sorted(d.items()))
desc = dict(sorted(d.items(), reverse=True))

print("Ascending by keys:", asc)
print("Descending by keys:", desc)

