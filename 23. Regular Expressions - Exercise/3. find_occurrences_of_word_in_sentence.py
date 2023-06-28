import re

sentence = input().lower()

searched_word = input().lower()

search_pattern = fr"\b({searched_word}+)\b"

result = re.findall(search_pattern, sentence)

print(len(result))
