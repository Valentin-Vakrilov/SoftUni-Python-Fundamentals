numbers_sequence = input().split()

numbers_as_int = []

for number in numbers_sequence:
    numbers_as_int.append(int(number))

result = sorted(numbers_as_int)
print(result)
