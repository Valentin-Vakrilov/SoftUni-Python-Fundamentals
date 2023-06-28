numbers_sequence = list(map(int, input().split(", ")))

max_number = max(numbers_sequence)

if max_number % 10 == 0:
    number_of_groups = int(max_number / 10)
else:
    number_of_groups = int((max_number / 10) + 1)

boundary = 10

for group in range(1, number_of_groups+1):
    group_numbers = list(filter(lambda x: x <= boundary, numbers_sequence))
    print(f"Group of {group * 10}'s: {group_numbers}")
    for number in group_numbers:
        numbers_sequence.remove(number)

    boundary += 10
