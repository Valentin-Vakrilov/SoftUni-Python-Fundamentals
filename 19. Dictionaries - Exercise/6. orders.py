items_dict_quantity = {}
items_dict_price = {}

command = input()

while command != "buy":
    current_command = command.split()
    product = current_command[0]
    price = float(current_command[1])
    quantity = int(current_command[2])
    if product not in items_dict_quantity:
        items_dict_quantity[product] = quantity
        items_dict_price[product] = price
    else:
        items_dict_quantity[product] += quantity
        items_dict_price[product] = price
    command = input()

for key, value in items_dict_quantity.items():
    total_price = value * items_dict_price[key]
    print(f"{key} -> {total_price:.2f}")
