import re

search_pattern = r"\b_([A-Za-z0-9]+)\b"

sentence = input()

matches = re.findall(search_pattern, sentence)

print(",".join(matches))
