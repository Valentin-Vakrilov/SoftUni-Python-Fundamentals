import re

search_pattern = r'\+359 2 [0-9]{3} [0-9]{4}|\+359-2-[0-9]{3}-[0-9]{4}\b'

phone_numbers = input()

result = re.findall(search_pattern, phone_numbers)

print(", ".join(result))
