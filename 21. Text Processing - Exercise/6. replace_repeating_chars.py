text = input()

new_text = ""

for char in range(len(text)):
    if char < len(text)-1:
        if text[char] == text[char+1]:
            continue
        else:
            new_text += text[char]
    elif char == len(text) - 1:
        new_text += text[char]

print(new_text)
