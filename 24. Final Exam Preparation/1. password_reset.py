string = input()

command = input()

new_string = string

while command != "Done":
    current_command = command.split()

    if current_command[0] == "TakeOdd":
        current_string = new_string
        new_string = ""
        for index in range(len(current_string)):
            if index % 2 != 0:
                new_string += current_string[index]
        print(new_string)
    elif current_command[0] == "Cut":
        start_index = int(current_command[1])
        length = int(current_command[2])
        end_index = start_index + length
        new_string = new_string[:start_index]+new_string[end_index:]
        print(new_string)
    elif current_command[0] == "Substitute":
        substring = current_command[1]
        substitute = current_command[2]
        if substring in new_string:
            new_string = new_string.replace(substring, substitute)
            print(new_string)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {new_string}")
