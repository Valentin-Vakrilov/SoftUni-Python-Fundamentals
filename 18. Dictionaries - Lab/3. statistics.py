products_dict = {}

command = input()

while command != "statistics":
    current_command = command.split(": ")
    product = current_command[0]
    quantity = current_command[1]
    if product in products_dict:
        products_dict[product] += int(quantity)
    else:
        products_dict[product] = int(quantity)

    command = input()

print("Products in stock:")
for product, quantity in products_dict.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products_dict.keys())}")
print(f"Total Quantity: {sum(products_dict.values())}")
