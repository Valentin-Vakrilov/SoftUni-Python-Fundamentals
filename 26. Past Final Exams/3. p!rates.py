def towns_func(towns, command):
    while command != "Sail":
        current_command = command.split("||")
        town = current_command[0]
        population = int(current_command[1])
        gold = int(current_command[2])

        if town not in towns:
            towns[town] = {"population": population, "gold": gold}
        else:
            towns[town]["population"] += population
            towns[town]["gold"] += gold

        command = input()

    return towns


def events_func(event, towns):
    while event != "End":
        current_command = event.split("=>")
        current_event = current_command[0]
        town = current_command[1]

        if current_event == "Plunder":
            population = int(current_command[2])
            gold = int(current_command[3])

            towns[town]["population"] -= population
            towns[town]["gold"] -= gold
            print(f"{town} plundered! {gold} gold stolen, {population} citizens killed.")

            if towns[town]["population"] <= 0 or towns[town]["gold"] <= 0:
                print(f"{town} has been wiped off the map!")
                del towns[town]

        elif current_event == "Prosper":
            gold = int(current_command[2])

            if gold > 0:
                towns[town]["gold"] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {towns[town]['gold']} gold.")
            else:
                print(f"Gold added cannot be a negative number!")

        event = input()


def print_func(towns):
    if len(towns) == 0:
        print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
    else:
        print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
        for town in towns:
            print(f"{town} -> Population: {towns[town]['population']} citizens, Gold: {towns[town]['gold']} kg")


command = input()
towns = {}
towns_func(towns, command)
event = input()
events_func(event, towns)
print_func(towns)
