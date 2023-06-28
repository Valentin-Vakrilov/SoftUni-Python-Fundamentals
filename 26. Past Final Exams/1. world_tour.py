route = input()

command = input()

while command != "Travel":
    current_command = command.split(":")
    current_action = current_command[0]

    if current_action == "Add Stop":
        index = int(current_command[1])
        string = current_command[2]

        if index in range(len(route)):
            route = route[:index] + string + route[index:]
        print(f"{route}")

    elif current_action == "Remove Stop":
        start_index = int(current_command[1])
        end_index = int(current_command[2])

        if start_index in range(len(route)) and end_index in range(len(route)):
            route = route[:start_index] + route[end_index+1:]
        print(f"{route}")

    elif current_action == "Switch":
        old_string = current_command[1]
        new_string = current_command[2]

        if old_string in route:
            route = route.replace(old_string, new_string)
        print(f"{route}")

    command = input()

print(f"Ready for world tour! Planned stops: {route}")
