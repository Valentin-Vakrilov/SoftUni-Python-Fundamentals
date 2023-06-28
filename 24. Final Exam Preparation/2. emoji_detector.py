import re

string = input()

threshold = 1

cool_emojis = []

for char in range(len(string)):
    if string[char].isdigit():
        threshold *= int(string[char])

search_pattern = r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*"

matches = re.findall(search_pattern, string)

for match in matches:
    current_threshold = 0
    for index in range(len(match)):
        if match[index].isalpha():
            current_threshold += ord(match[index])
    if current_threshold >= threshold:
        cool_emojis.append(match)

print(f"Cool threshold: {threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
print('\n'.join(cool_emojis))
