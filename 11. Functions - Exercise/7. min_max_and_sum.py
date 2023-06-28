numbers = input().split()

numbers_as_int = []

for current_number in numbers:
    numbers_as_int.append(int(current_number))

min_result = min(numbers_as_int)
max_result = max(numbers_as_int)
sum_result = sum(numbers_as_int)

print(f"The minimum number is {min_result}")
print(f"The maximum number is {max_result}")
print(f"The sum number is: {sum_result}")
