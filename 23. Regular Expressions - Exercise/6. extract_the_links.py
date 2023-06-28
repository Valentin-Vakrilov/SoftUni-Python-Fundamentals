import re

search_pattern = r"(www\.[A-Za-z0-9\-]+(\.[a-z]+)+)"

sentence = input()

valid_links = []

while sentence:
    match = re.search(search_pattern, sentence)
    if match:
        valid_links.append(match.group(1))

    sentence = input()

for link in valid_links:
    print(link)
