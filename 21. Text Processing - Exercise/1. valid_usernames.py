def valid_length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def valid_symbols(username):
    for char in username:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True


def redundant_symbols_check(username):
    if " " in username:
        return False
    return True


usernames = input().split(", ")

for username in usernames:
    if valid_length(username) and valid_symbols(username) and redundant_symbols_check(username):
        print(username)
