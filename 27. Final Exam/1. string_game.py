string = input()

command = input()

while command != "Done":
    current_command = command.split()

    if current_command[0] == "Change":
        char = current_command[1]
        replacement = current_command[2]
        while char in string:
            string = string.replace(char, replacement)
        print(string)
    elif current_command[0] == "Includes":
        substring = current_command[1]
        if substring in string:
            print("True")
        else:
            print("False")
    elif current_command[0] == "End":
        end_string = current_command[1]
        reversed_string = string[::-1]
        string_ending = reversed_string[:len(end_string)]
        if end_string == string_ending:
            print("True")
        else:
            print("False")
    elif current_command[0] == "Uppercase":
        string = string.upper()
        print(string)
    elif current_command[0] == "FindIndex":
        current_char = current_command[1]
        print(string.find(current_char))
    elif current_command[0] == "Cut":
        start_index = int(current_command[1])
        count = int(current_command[2])
        string = string[start_index:start_index+count]
        print(string)

    command = input()
