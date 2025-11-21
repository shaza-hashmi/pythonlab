nums = list(map(int, input("Enter numbers: ").split()))
print("Positive:", [n for n in nums if n > 0])

n = int(input("Enter N: "))
print("Squares:", [i*i for i in range(1, n+1)])

word = input("Enter word: ")
print("Vowels:", [c for c in word if c.lower() in 'aeiou'])
print("Ordinals:", [ord(c) for c in word])

