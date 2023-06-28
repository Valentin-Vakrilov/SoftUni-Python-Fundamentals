import re


text = input()

search_pattern = r"@([A-Za-z]{3,})@@([A-Za-z]{3,})@|#([A-Za-z]{3,})##([A-Za-z]{3,})#"

matches = re.finditer(search_pattern, text)

valid_matches = []

mirror_words = []

for match in matches:
    current_match = match.group(0)
    valid_matches.append(current_match)
    if "##" in current_match:
        splitted_match = current_match.split("##")
        left_part = splitted_match[0]
        right_part = splitted_match[1]
        if left_part == right_part[::-1]:
            mirror_words.append(left_part[1:] + " <=> " + right_part[:-1])
    elif "@@" in current_match:
        splitted_match = current_match.split("@@")
        left_part = splitted_match[0]
        right_part = splitted_match[1]
        if left_part == right_part[::-1]:
            mirror_words.append(left_part[1:] + " <=> " + right_part[:-1])

if len(valid_matches) > 0:
    print(f"{len(valid_matches)} word pairs found!")
else:
    print("No word pairs found!")

if len(mirror_words) > 0:
    print(f"The mirror words are:")
    print(f"{', '.join(mirror_words)}")
else:
    print("No mirror words!")
