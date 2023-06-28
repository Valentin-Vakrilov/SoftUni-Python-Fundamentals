import re

search_pattern = r"\d+"

sentence = input()

while True:
    if sentence:
        matches = re.findall(search_pattern, sentence)
        if matches:
            print(" ".join(matches), end=" ")
    else:
        break

    sentence = input()
