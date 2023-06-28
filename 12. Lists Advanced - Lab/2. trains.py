number_of_wagons = int(input())

train_list = [0] * number_of_wagons

command = input()

while command != "End":
    current_command = command.split(" ")

    if current_command[0] == "add":
        people_to_add = int(current_command[1])
        train_list[-1] += people_to_add

    elif current_command[0] == "insert":
        wagon_number = int(current_command[1])
        people_added = int(current_command[2])
        train_list[wagon_number] += people_added

    elif current_command[0] == "leave":
        wagon_number = int(current_command[1])
        people_to_remove = int(current_command[2])
        train_list[wagon_number] -= people_to_remove

    command = input()

print(train_list)
