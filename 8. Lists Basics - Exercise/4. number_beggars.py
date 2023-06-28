sums_for_beggars = input().split(", ")
count_of_beggars = int(input())

final_list = []
index_counter = 0

sums_for_beggars_as_int = []

for current_sum in sums_for_beggars:
    sums_for_beggars_as_int.append(int(current_sum))

while index_counter < count_of_beggars:
    sum_for_current_beggar = 0
    for index in range(index_counter, len(sums_for_beggars_as_int), count_of_beggars):
        sum_for_current_beggar += sums_for_beggars_as_int[index]
    index_counter += 1
    final_list.append(sum_for_current_beggar)

print(final_list)
