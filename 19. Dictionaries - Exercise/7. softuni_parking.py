parking_dict = {}

number_of_commands = int(input())

for command in range(number_of_commands):
    current_command = input().split()
    if current_command[0] == "register":
        user = current_command[1]
        licence_plate = current_command[2]
        if user not in parking_dict:
            parking_dict[user] = licence_plate
            print(f"{user} registered {parking_dict[user]} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_dict[user]}")
    elif current_command[0] == "unregister":
        user = current_command[1]
        if user not in parking_dict:
            print(f"ERROR: user {user} not found")
        else:
            del parking_dict[user]
            print(f"{user} unregistered successfully")

for user, licence_plate in parking_dict.items():
    print(f"{user} => {parking_dict[user]}")
