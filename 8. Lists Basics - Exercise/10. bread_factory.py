events = input().split("|")

initial_energy = 100
initial_coins = 100

events_completed = True

for event in events:
    current_event = event.split("-")
    current_action = current_event[0]
    current_value = int(current_event[1])
    if current_action == "rest":
        temporary_energy = initial_energy
        initial_energy += current_value
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - temporary_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif current_action == "order":
        if initial_energy >= 30:
            initial_coins += current_value
            initial_energy -= 30
            print(f"You earned {current_value} coins.")
        else:
            initial_energy += 50
            if initial_energy > 100:
                initial_energy = 100
            print("You had to rest!")
    else:
        if initial_coins >= current_value:
            initial_coins -= current_value
            print(f"You bought {current_action}.")
        else:
            print(f"Closed! Cannot afford {current_action}.")
            events_completed = False
            break

if events_completed:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
