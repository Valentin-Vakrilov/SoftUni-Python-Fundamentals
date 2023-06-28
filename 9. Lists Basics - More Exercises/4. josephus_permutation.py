people = input().split()
key = int(input())

executed_list = []
executed_counter = 0

index = 0

while len(people) > 0:
    executed_counter += 1

    if executed_counter % key == 0:
        executed_list.append(people.pop(index))
    else:
        index += 1

    if index >= len(people):
        index = 0

final_list = list(map(int, executed_list))
print(str(final_list).replace(" ", ""))
