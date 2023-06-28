command = input()

to_do_list = [0] * 10

while True:
    if command == "End":
        break

    current_command = command.split("-")

    importance = int(current_command[0]) - 1
    task = current_command[1]

    to_do_list.pop(importance)
    to_do_list.insert(importance, task)

    command = input()

final_list = [task for task in to_do_list if task != 0]

print(final_list)
