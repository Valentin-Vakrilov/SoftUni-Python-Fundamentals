inventory = input().split()

inventory_dict = {}

for item in range(0, len(inventory), 2):
    food = inventory[item]
    quantity = inventory[item + 1]
    inventory_dict[food] = int(quantity)

print(inventory_dict)
