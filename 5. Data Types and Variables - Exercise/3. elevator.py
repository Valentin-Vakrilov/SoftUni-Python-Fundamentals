number_of_people = int(input())
capacity = int(input())

first_result = number_of_people // capacity

second_result = number_of_people % capacity

if second_result != 0:
    first_result += 1

print(first_result)
