message = input()

command = input()

while command != "Decode":
    current_command = command.split("|")

    if current_command[0] == "Move":
        number_of_letters = int(current_command[1])
        message = message[number_of_letters:] + message[:number_of_letters]

    elif current_command[0] == "Insert":
        index = int(current_command[1])
        value = current_command[2]
        message = message[:index] + value + message[index:]

    elif current_command[0] == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        if substring in message:
            message = message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")
