message = input().split()

decoded_message = []

for word in message:
    current_word = ''
    current_digit = ''
    for i in word:
        if i.isdigit():
            current_digit += i
            word = word.replace(i, "")
    current_word += chr(int(current_digit))
    new_word = len(word)
    if len(word) >= 2:
        current_word += word[-1] + word[1:-1] + word[0]
    else:
        current_word += word[0]

    decoded_message.append(current_word)

print(' '.join(decoded_message))
