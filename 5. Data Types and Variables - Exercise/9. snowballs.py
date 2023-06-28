import sys

number_of_snowballs = int(input())

snowball_weight = - sys.maxsize
time_needed = - sys.maxsize
quality_of_snowball = - sys.maxsize
snowball_value = ""

highest_value = - sys.maxsize

for snowball in range(number_of_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())

    snowball_value = int((current_weight / current_time) ** current_quality)

    if snowball_value > highest_value:
        highest_value = snowball_value
        snowball_weight = current_weight
        time_needed = current_time
        quality_of_snowball = current_quality

print(f"{snowball_weight} : {time_needed} = {highest_value} ({quality_of_snowball})")
