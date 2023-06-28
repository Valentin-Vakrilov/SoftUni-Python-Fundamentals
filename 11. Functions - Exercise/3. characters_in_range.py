def return_characters(first, second):
    char_list = []
    for current_character in range(ord(first) + 1, ord(second)):
        char_list.append(chr(current_character))
    return char_list


first_character = input()
second_character = input()
result = return_characters(first_character, second_character)
print(" ".join(result))
