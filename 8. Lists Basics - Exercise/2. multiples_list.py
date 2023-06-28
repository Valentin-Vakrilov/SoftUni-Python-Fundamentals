factor = int(input())
count = int(input())

current_number = 0
multiples_list = []

for number in range(count):
    current_number += factor
    multiples_list.append(current_number)

print(multiples_list)
