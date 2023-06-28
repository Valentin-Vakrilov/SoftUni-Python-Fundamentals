given_numbers = list(map(int, input().split()))
command = input()

while command != "Finish":
    current_command = command.split()
    if current_command[0] == "Add":
        given_numbers.append(int(current_command[1]))
    elif current_command[0] == "Remove":
        given_numbers.remove(int(current_command[1]))
    elif current_command[0] == "Replace":
        for number in given_numbers:
            if number == int(current_command[1]):
                searched_element = given_numbers.index(int(current_command[1]))
                given_numbers.pop(searched_element)
                given_numbers.insert(searched_element, int(current_command[2]))
                break
    elif current_command[0] == "Collapse":
        given_numbers = [num for num in given_numbers if num >= int(current_command[1])]

    command = input()

print(*given_numbers, sep=" ")
