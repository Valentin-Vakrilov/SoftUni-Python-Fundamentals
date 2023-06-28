import re

search_pattern = r'\b(\d{2})([\.\-\/])([A-Z][a-z]{2})\2(\d{4})\b'

dates = input()

result = re.findall(search_pattern, dates)

for current_result in result:
    print(f"Day: {current_result[0]}, Month: {current_result[2]}, Year: {current_result[3]}")
