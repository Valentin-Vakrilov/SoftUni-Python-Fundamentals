first_index = int(input())
second_index = int(input())

for character in range(first_index, second_index+1):
    current_character = chr(character)
    print(current_character, end=" ")
