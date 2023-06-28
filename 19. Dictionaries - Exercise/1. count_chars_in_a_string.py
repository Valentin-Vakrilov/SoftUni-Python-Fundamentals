char_dict = {}

string = input()

for [i] in string:
    if i == " ":
        pass
    else:
        key = i
        if key not in char_dict:
            char_dict[key] = 0
        char_dict[key] += 1

for key in char_dict:
    print(f"{key} -> {char_dict[key]}")
