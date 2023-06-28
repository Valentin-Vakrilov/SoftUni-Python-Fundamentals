given_list = input().split(", ")

ascii_dict = {key: ord(key) for key in given_list}

print(ascii_dict)
