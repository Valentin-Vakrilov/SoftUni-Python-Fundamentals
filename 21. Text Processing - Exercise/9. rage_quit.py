text = input().upper()

current_text = ""
new_text = ""
multiplier = ""
unique_symbols_counter = 0

for char in range(len(text)):
    if not text[char].isdigit():
        current_text += text[char]
    else:
        for check_next_char in range(char, len(text)):
            if not text[check_next_char].isdigit():
                break
            else:
                multiplier += text[check_next_char]
        new_text += current_text * int(multiplier)
        current_text = ""
        multiplier = ""

    if not text[char] in new_text and text[char] in current_text:
        unique_symbols_counter += 1

print(f"Unique symbols used: {unique_symbols_counter}")  # else you could use set as well set(len(new_text))
print(new_text)
