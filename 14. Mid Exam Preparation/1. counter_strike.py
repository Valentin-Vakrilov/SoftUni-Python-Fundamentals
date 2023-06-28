initial_energy = int(input())
command = input()

won_battles_counter = 0

while command != "End of battle" and initial_energy >= int(command):
    initial_energy -= int(command)
    won_battles_counter += 1

    if won_battles_counter % 3 == 0:
        initial_energy += won_battles_counter

    command = input()

if command == "End of battle":
    print(f"Won battles: {won_battles_counter}. Energy left: {initial_energy}")
else:
    print(f"Not enough energy! Game ends with {won_battles_counter} won battles and {initial_energy} energy")
