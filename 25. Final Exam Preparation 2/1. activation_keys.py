string = input()

command = input()

while command != "Generate":
    current_command = command.split(">>>")

    if current_command[0] == "Contains":
        substring = current_command[1]
        if substring in string:
            print(f"{string} contains {substring}")
        else:
            print("Substring not found!")
    elif current_command[0] == "Flip":
        if current_command[1] == "Upper":
            string = string[:int(current_command[2])] + string[int(current_command[2]):int(current_command[3])].upper()\
                     + string[int(current_command[3]):]
            print(string)
        elif current_command[1] == "Lower":
            string = string[:int(current_command[2])] + string[int(current_command[2]):int(current_command[3])].lower()\
                     + string[int(current_command[3]):]
            print(string)
    elif current_command[0] == "Slice":
        string = string[:int(current_command[1])]+string[int(current_command[2]):]
        print(string)

    command = input()

print(f"Your activation key is: {string}")
