import re


string = input()

search_pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2,2}\/\d{2,2}\/\d{2,2})\1(\d{1,5})\1"

matches = re.finditer(search_pattern, string)

total_calories = 0

foods_list = []

for match in matches:
    food = match.group(2)
    expiration_date = match.group(3)
    calories = match.group(4)
    foods_list.append([food, expiration_date, calories])
    total_calories += int(calories)

number_of_days = total_calories // 2000

print(f"You have food to last you for: {number_of_days} days!")

for food in foods_list:
    print(f"Item: {food[0]}, Best before: {food[1]}, Nutrition: {food[2]}")
