def password_length(password):
    if 6 <= len(password) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def password_only_digits_and_letters(password):
    if password.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def password_must_have_two_digits(password):
    digits_counter = 0
    for current_symbol in password:
        if current_symbol.isdigit():
            digits_counter += 1
    if digits_counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


given_password = input()
valid_password = [password_length(given_password), password_only_digits_and_letters(given_password),
                  password_must_have_two_digits(given_password)]
if all(valid_password):
    print("Password is valid")
