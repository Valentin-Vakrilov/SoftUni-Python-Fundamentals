def hero_commands(heroes_dict, command):
    while True:
        if command == "End":
            break

        current_command = command.split()
        action = current_command[0]
        hero = current_command[1]

        if action == "Enroll":
            if hero not in heroes_dict:
                heroes_dict[hero] = ""
            else:
                print(f"{hero} is already enrolled.")
        elif action == "Learn":
            learn_spell = current_command[2]
            if hero not in heroes_dict:
                print(f"{hero} doesn't exist.")
            else:
                if learn_spell in heroes_dict[hero]:
                    print(f"{hero} has already learnt {learn_spell}.")
                else:
                    heroes_dict[hero] = learn_spell
        elif action == "Unlearn":
            unlearn_spell = current_command[2]
            if hero not in heroes_dict:
                print(f"{hero} doesn't exist.")
            else:
                if unlearn_spell not in heroes_dict[hero]:
                    print(f"{hero} doesn't know {unlearn_spell}.")
                else:
                    heroes_dict[hero].pop(0)

        command = input()

    return heroes_dict


def heroes_print(heroes_dict):
    print("Heroes:")
    for hero in heroes_dict:
        if len(heroes_dict[hero]) > 0:
            print(f"== {hero}: {heroes_dict[hero]}")
        elif len(heroes_dict[hero]) == 0:
            print(f"== {hero}: ")


command = input()
heroes_dict = {}
hero_commands(heroes_dict, command)
heroes_print(heroes_dict)
