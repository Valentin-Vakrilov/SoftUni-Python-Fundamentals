text = input()

new_text = ""

for index in range(len(text)):
    new_text += chr(ord(text[index]) + 3)

print(new_text)
