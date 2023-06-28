inventory = input().split()

inventory_dict = {}

for item in range(0, len(inventory), 2):
    food = inventory[item]
    quantity = inventory[item + 1]
    inventory_dict[food] = int(quantity)

searched_items = input().split()

for current_item in searched_items:
    if current_item in inventory_dict:
        print(f"We have {inventory_dict[current_item]} of {current_item} left")
    else:
        print(f"Sorry, we don't have {current_item}")
