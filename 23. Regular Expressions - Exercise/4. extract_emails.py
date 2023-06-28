import re

search_pattern = r" ([A-Za-z0-9]+[\.\-\_]*[A-Za-z0-9]+@[A-Za-z\-]+(\.[A-Za-z\-]+)+)\b"

sentence = input()

matches = re.findall(search_pattern, sentence)

for match in matches:
    print(match[0])
