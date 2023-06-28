number = int(input())
word = input()

first_list = []
second_list = []

for string in range(number):
    current_string = input()
    first_list.append(current_string)
print(first_list)

for new_string in range(number):
    if word in first_list[new_string]:
        second_list.append(first_list[new_string])
print(second_list)
