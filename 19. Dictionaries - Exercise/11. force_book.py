force_users_dict = {}

command = input()

while command != "Lumpawaroo":
    if "|" in command:
        current_command = command.split(" | ")
        side, user = current_command
        present = False
        for value in force_users_dict.values():
            if user in value:
                present = True
                break
        if not present:
            if side not in force_users_dict.keys():
                force_users_dict[side] = [user]
            else:
                force_users_dict[side].append(user)
    else:
        current_command = command.split(" -> ")
        user, side = current_command
        for key, value in force_users_dict.items():
            if user in value:
                force_users_dict[key].pop(value.index(user))
                break
        if side not in force_users_dict.keys():
            force_users_dict[side] = [user]
        else:
            force_users_dict[side] += [user]
        print(f"{user} joins the {side} side!")
    command = input()

for side in force_users_dict.keys():
    if len(force_users_dict[side]) > 0:
        print(f"Side: {side}, Members: {len(force_users_dict[side])}")
        [print(f"! {user}") for user in force_users_dict[side]]
