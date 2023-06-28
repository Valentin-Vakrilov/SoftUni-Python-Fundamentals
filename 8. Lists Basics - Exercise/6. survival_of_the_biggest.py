list_of_numbers = input().split()
numbers_to_remove = int(input())

list_of_numbers_as_int = []
final_list = ""

for current_number in list_of_numbers:
    list_of_numbers_as_int.append(int(current_number))

for number in range(numbers_to_remove):
    min_number = min(list_of_numbers_as_int)
    list_of_numbers_as_int.remove(min_number)

for index in list_of_numbers_as_int:
    final_list += str(index) + ", "

print(final_list[0:-2])
