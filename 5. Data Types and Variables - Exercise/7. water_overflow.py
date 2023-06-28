water_tank_capacity = 255

number_of_lines = int(input())

total_water = 0

for i in range(number_of_lines):
    current_quantity = int(input())
    if current_quantity + total_water > water_tank_capacity:
        print("Insufficient capacity!")
        continue
    else:
        total_water += current_quantity

print(total_water)
