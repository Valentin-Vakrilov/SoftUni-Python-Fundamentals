items_dict = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
items_list = input().split()

while not obtained:
    for current_item in range(0, len(items_list), 2):
        item_name = items_list[current_item + 1].lower()
        item_quantity = int(items_list[current_item])
        if item_name not in items_dict:
            items_dict[item_name] = 0
        items_dict[item_name] += item_quantity
        if items_dict["shards"] >= 250:
            print("Shadowmourne obtained!")
            items_dict["shards"] -= 250
            obtained = True
        elif items_dict["fragments"] >= 250:
            print("Valanyr obtained!")
            items_dict["fragments"] -= 250
            obtained = True
        elif items_dict["motes"] >= 250:
            print("Dragonwrath obtained!")
            items_dict["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break

    items_list = input().split()

for item, quantity in items_dict.items():
    print(f"{item}: {items_dict[item]}")
