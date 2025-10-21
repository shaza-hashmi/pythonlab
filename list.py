list1 = list(map(int,input("Enter First list:").split()))
list2 = list(map(int,input("Enter Second list:").split()))


print("Same Length?",len(list1) == len(list2))
print("Same Sum?",sum(list1) == sum(list2))


common = set(list1) & set(list2)
print("Common values:",common if common else "None")

