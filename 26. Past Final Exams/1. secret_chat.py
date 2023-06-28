string = input()

while True:
    command = input()

    if command == "Reveal":
        break

    current_command = command.split(":|:")
    current_action = current_command[0]

    if current_action == "InsertSpace":
        index = int(current_command[1])
        string = string[:index] + " " + string[index:]
        print(string)

    elif current_action == "Reverse":
        substring = current_command[1]
        if substring in string:
            string = string.replace(substring, "", 1)
            reversed_substring = substring[::-1]
            string += reversed_substring
            print(string)
        else:
            print("error")

    elif current_action == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        while substring in string:
            string = string.replace(substring, replacement)
        print(string)

print(f"You have a new text message: {string}")
