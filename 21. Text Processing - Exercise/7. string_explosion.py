text = input()

new_text = ""

strength = 0

for char in range(len(text)):
    if strength > 0 and text[char] != ">":
        strength -= 1
    elif text[char] == ">":
        new_text += text[char]
        strength += int(text[char+1])
    else:
        new_text += text[char]

print(new_text)
