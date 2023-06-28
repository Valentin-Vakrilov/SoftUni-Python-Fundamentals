text = input()

# my_solution
char = len(text)

reversed_text = ""
for i in range(char-1, -1, -1):
    reversed_text += text[i]

print(reversed_text)

# short_solution
# print(text[::-1])