import re

search_patten = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

names = input()

result = re.findall(search_patten, names)

print(" ".join(result))
