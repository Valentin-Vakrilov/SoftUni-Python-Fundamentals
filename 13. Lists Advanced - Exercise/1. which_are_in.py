first_list = input().split(", ")
second_list = input().split(", ")

substrings_list = []

for first_word in first_list:
    for second_word in second_list:
        if first_word in second_word:
            substrings_list.append(first_word)
            break

print(substrings_list)
