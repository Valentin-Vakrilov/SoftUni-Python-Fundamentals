fire_cells = input().split("#")
water_quantity = int(input())

total_effort = 0
total_fire = 0
print("Cells:")

for fire in fire_cells:
    splitting_fire = fire.split(" ")
    current_fire = splitting_fire[0]
    current_level_of_fire = int(splitting_fire[2])
    if water_quantity >= current_level_of_fire:
        if current_fire == "High" and 81 <= current_level_of_fire <= 125:
            water_quantity -= current_level_of_fire
            effort = current_level_of_fire * 0.25
            total_effort += effort
            total_fire += current_level_of_fire
            print(f" - {current_level_of_fire}")
        elif current_fire == "Medium" and 51 <= current_level_of_fire <= 80:
            water_quantity -= current_level_of_fire
            effort = current_level_of_fire * 0.25
            total_effort += effort
            total_fire += current_level_of_fire
            print(f" - {current_level_of_fire}")
        elif current_fire == "Low" and 1 <= current_level_of_fire <= 50:
            water_quantity -= current_level_of_fire
            effort = current_level_of_fire * 0.25
            total_effort += effort
            total_fire += current_level_of_fire
            print(f" - {current_level_of_fire}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
