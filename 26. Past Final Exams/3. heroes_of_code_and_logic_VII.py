def heroes(heroes_dict, number):
    for hero in range(number):
        current_hero = input().split()
        hero_name = current_hero[0]
        hit_points = int(current_hero[1])
        mana_points = int(current_hero[2])

        heroes_dict[hero_name] = {"hit_points": hit_points, "mana_points": mana_points}

    return heroes_dict


def actions(heroes_dict):
    while True:
        command = input()

        if command == "End":
            break

        current_action = command.split(" - ")
        action_name = current_action[0]
        hero_name = current_action[1]

        if action_name == "CastSpell":
            mana_points_needed = int(current_action[2])
            spell_name = current_action[3]

            if heroes_dict[hero_name]["mana_points"] >= mana_points_needed:
                heroes_dict[hero_name]["mana_points"] -= mana_points_needed
                print(f"{hero_name} has successfully cast {spell_name} \
and now has {heroes_dict[hero_name]['mana_points']} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif action_name == "TakeDamage":
            damage = int(current_action[2])
            attacker = current_action[3]

            heroes_dict[hero_name]["hit_points"] -= damage

            if heroes_dict[hero_name]["hit_points"] > 0:
                print(f"{hero_name} was hit for {damage} HP by {attacker} \
and now has {heroes_dict[hero_name]['hit_points']} HP left!")
            else:
                print(f"{hero_name} has been killed by {attacker}!")
                del heroes_dict[hero_name]

        elif action_name == "Recharge":
            amount = int(current_action[2])

            if heroes_dict[hero_name]["mana_points"] + amount > 200:
                charged_amount = 200 - heroes_dict[hero_name]["mana_points"]
                heroes_dict[hero_name]["mana_points"] = 200
                print(f"{hero_name} recharged for {charged_amount} MP!")
            else:
                heroes_dict[hero_name]["mana_points"] += amount
                print(f"{hero_name} recharged for {amount} MP!")

        elif action_name == "Heal":
            amount = int(current_action[2])

            if heroes_dict[hero_name]["hit_points"] + amount > 100:
                charged_amount = 100 - heroes_dict[hero_name]["hit_points"]
                heroes_dict[hero_name]["hit_points"] = 100
                print(f"{hero_name} healed for {charged_amount} HP!")
            else:
                heroes_dict[hero_name]["hit_points"] += amount
                print(f"{hero_name} healed for {amount} HP!")


def print_heroes(heroes_dict):
    for hero in heroes_dict:
        hit_points = heroes_dict[hero]["hit_points"]
        mana_points = heroes_dict[hero]["mana_points"]

        print(f"{hero}")
        print(f"  HP: {hit_points}")
        print(f"  MP: {mana_points}")


def heroes_of_code_and_logic(number):
    heroes_dict = {}

    heroes(heroes_dict, number)
    actions(heroes_dict)
    print_heroes(heroes_dict)


number_of_heroes = int(input())
heroes_of_code_and_logic(number_of_heroes)
