given_string = input()

capital_letter_indices = []

for char in range(len(given_string)):
    current_char = given_string[char]
    if current_char.isupper():
        capital_letter_indices.append(char)

print(capital_letter_indices)
