number = int(input())

for first_character in range(97, 97+number):
    first_character = chr(first_character)
    for second_character in range(97, 97+number):
        second_character = chr(second_character)
        for third_character in range(97, 97+number):
            third_character = chr(third_character)
            print(f"{first_character}{second_character}{third_character}")
