number = int(input())

all_list = []
even_list = []
odd_list = []
negative_list = []
positive_list = []

for i in range(number):
    current_number = int(input())
    all_list.append(current_number)

command = input()

for new_number in range(number):
    current_new_number = all_list[new_number]
    if current_new_number % 2 == 0:
        even_list.append(current_new_number)
    else:
        odd_list.append(current_new_number)
    if current_new_number < 0:
        negative_list.append(current_new_number)
    else:
        positive_list.append(current_new_number)

if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "negative":
    print(negative_list)
elif command == "positive":
    print(positive_list)
