numbers = input().split()

numbers_as_int = []

for current_number in numbers:
    numbers_as_int.append(int(current_number))

is_even_condition = lambda number: number % 2 == 0
result = list(filter(is_even_condition, numbers_as_int))
print(result)
