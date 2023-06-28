quantity_of_decorations = int(input())
days_left = int(input())

cost_of_order = 0
total_order_cost = 0
total_spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
ornament_set_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity_of_decorations = quantity_of_decorations + 2
    if day % 2 == 0:
        cost_of_order = quantity_of_decorations * ornament_set_price
        total_order_cost += cost_of_order
        total_spirit += ornament_set_points
    if day % 3 == 0:
        cost_of_order = quantity_of_decorations * tree_skirt_price + quantity_of_decorations * tree_garland_price
        total_order_cost += cost_of_order
        total_spirit = total_spirit + tree_skirt_points + tree_garland_points
    if day % 5 == 0:
        cost_of_order = quantity_of_decorations * tree_lights_price
        total_order_cost += cost_of_order
        total_spirit += tree_lights_points

    if day % 5 == 0 and day % 3 == 0:
        total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20
        total_order_cost = total_order_cost + tree_skirt_price + tree_garland_price + tree_lights_price

if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_order_cost}")
print(f"Total spirit: {total_spirit}")
