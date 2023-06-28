import re

search_pattern = r">>([A-Za-z]+)<<([0-9]+|[0-9]+\.?[0-9]+)!([0-9]+)"

command = input()

bought_furniture = []

total_cost = 0

while command != "Purchase":
    match = re.search(search_pattern, command)
    if match:
        furniture = match.group(1)
        price = match.group(2)
        quantity = match.group(3)
        # or
        # furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_cost += int(quantity) * float(price)

    command = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
