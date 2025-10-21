str1 = input("enter first string:")
str2 = input("enter second string:")


new_str1 =str1[0] +str2[1] +str1[2:]
new_str2 =str2[0] +str1[1] +str2[2:]


result = new_str1  + "" +new_str2
print(result)
