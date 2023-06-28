words = input().split()

result = []

for word in words:
    repeated_word = word * len(word)
    result.append(repeated_word)

print("".join(result))
