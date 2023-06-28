import re

search_pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

numbers = input()

result = re.finditer(search_pattern, numbers)

for current_result in result:
    print(current_result.group(), end=" ")
