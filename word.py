text = input("enter a line of text:").split()

word_count = {}
for word in text:
    word_count[word] = word_count.get(word,0) + 1
print(word_count)
