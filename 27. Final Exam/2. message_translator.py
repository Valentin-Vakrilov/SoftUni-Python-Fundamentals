import re

count_of_strings = int(input())

search_pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"

for string in range(count_of_strings):
    current_string = input()
    match = re.search(search_pattern, current_string)
    if match:
        command = match.group(1)
        message = match.group(2)
        number_sequence = []
        for char in range(len(message)):
            current_char = ord(message[char])
            number_sequence.append(str(current_char))
        print(f"{command}: {' '.join(number_sequence)}")
    else:
        print("The message is invalid")
