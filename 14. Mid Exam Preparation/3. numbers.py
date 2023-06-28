def top_five_numbers(numbers):
    final_list = []
    average_value = sum(numbers) / len(numbers)
    greater_than_average_value = [num for num in numbers if num > average_value]
    sorted_numbers = sorted(greater_than_average_value)[::-1]

    for number in sorted_numbers:
        if len(final_list) < 5:
            final_list.append(number)

    return ' '.join(str(num) for num in final_list)


numbers_sequence = list(map(int, input().split()))
if len(top_five_numbers(numbers_sequence)) == 0:
    print("No")
else:
    print(top_five_numbers(numbers_sequence))


# def top_five_numbers(numbers):
#     final_list = []
#     average_value = sum(numbers) / len(numbers)
#     greater_than_average_value = [num for num in numbers if num > average_value]
#     if greater_than_average_numbers:
#         sorted_numbers = sorted(greater_than_average_value)[::-1]
#         for number in sorted_numbers:
#             if len(final_list) < 5:
#                 final_list.append(number)
#         print(" ".join(str(num) for num in final_list))
#     else:
#         print("No")
#
#
# numbers_sequence = list(map(int, input().split()))
# result = top_five_numbers(numbers_sequence)
