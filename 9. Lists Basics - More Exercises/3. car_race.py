import math

numbers_sequence = input().split()

middle = math.floor(len(numbers_sequence) / 2)

left_side = numbers_sequence[:middle]
right_side = numbers_sequence[middle+1:]

sorted_right_side = right_side[::-1]

left_car_time = 0

for time in left_side:
    if time == "0":
        left_car_time *= 0.8
    left_car_time += int(time)

right_car_time = 0

for time in sorted_right_side:
    if time == "0":
        right_car_time *= 0.8
    right_car_time += int(time)

if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")
