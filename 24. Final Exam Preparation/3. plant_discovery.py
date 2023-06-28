def plants_information(plants, number):
    for plant in range(number):
        command = input().split("<->")
        plant = command[0]
        rarity = int(command[1])

        if plant not in plants:
            plants[plant] = {"rarity": rarity, "rating": []}
        else:
            plants[plant]["rarity"] += rarity

    return plants


def plants_commands(plants):

    while True:
        current_command = input().split(": ")

        if current_command[0] == "Exhibition":
            break

        splitted_command = current_command[1].split(" - ")
        plant = splitted_command[0]
        if plant not in plants:
            print("error")
            continue

        if current_command[0] == "Rate":
            rating = int(splitted_command[1])
            plants[plant]["rating"].append(rating)
        elif current_command[0] == "Update":
            new_rarity = int(splitted_command[1])
            plants[plant]["rarity"] = new_rarity
        elif current_command[0] == "Reset":
            plants[plant]["rating"].clear()

    return plants


def print_func(plants):
    print("Plants for the exhibition:")

    for element in plants:
        if sum(plants[element]['rating']) != 0 and len(plants[element]['rating']) > 0:
            average_rating = sum(plants[element]['rating']) / len(plants[element]['rating'])
        else:
            average_rating = 0

        rarity = plants[element]["rarity"]

        print(f"- {element}; Rarity: {rarity}; Rating: {average_rating:.2f}")


def plant_discovery(number):
    plants_dict = {}

    plants_information(plants_dict, number)
    plants_commands(plants_dict)
    print_func(plants_dict)


number_of_plants = int(input())
plant_discovery(number_of_plants)
