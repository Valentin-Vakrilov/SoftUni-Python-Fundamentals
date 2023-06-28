number_sequence = input().split()

list_of_numbers = []

for number in number_sequence:
    current_number = float(number)
    list_of_numbers.append(current_number)

list_of_abs_numbers = []

for number in list_of_numbers:
    current_number = abs(number)
    list_of_abs_numbers.append(current_number)

print(list_of_abs_numbers)
