import sys

initial_list = list(map(int, input().split()))

command = input()

while command != 'end':
    current_command = command.split()
    if current_command[0] == 'exchange':
        if int(current_command[1]) > len(initial_list) or int(current_command[1]) < 0:
            print('Invalid index')
        first_list = initial_list[:int(current_command[1])+1]
        second_list = initial_list[int(current_command[1])+1:]
        initial_list = second_list + first_list
    elif current_command[0] == 'max':
        if current_command[1] == 'even':
            even_nums = [num for num in initial_list if num % 2 == 0]
            if len(even_nums) == 0:
                print("No matches")
            else:
                max_even_num = -sys.maxsize
                for number in even_nums[::-1]:
                    if number >= max_even_num:
                        max_even_num = number
                max_even_index = initial_list.index(max_even_num)
                print(f"{max_even_index}")
        elif current_command[1] == 'odd':
            odd_nums = [num for num in initial_list if num % 2 != 0]
            if len(odd_nums) == 0:
                print("No matches")
            else:
                max_odd_num = -sys.maxsize
                for number in odd_nums[::-1]:
                    if number > max_odd_num:
                        max_odd_num = number
                max_odd_index = initial_list.index(max_odd_num)
                print(f"{max_odd_index}")
    elif current_command[0] == 'min':
        if current_command[1] == 'even':
            even_nums = [num for num in initial_list if num % 2 == 0]
            if len(even_nums) == 0:
                print("No matches")
            else:
                min_even_num = sys.maxsize
                for number in even_nums[::-1]:
                    if number < min_even_num:
                        min_even_num = number
                min_even_index = initial_list.index(min_even_num)
                print(f"{min_even_index}")
        elif current_command[1] == 'odd':
            odd_nums = [num for num in initial_list if num % 2 != 0]
            if len(odd_nums) == 0:
                print("No matches")
            else:
                min_odd_num = sys.maxsize
                for number in odd_nums[::-1]:
                    if number < min_odd_num:
                        min_odd_num = number
                min_odd_index = initial_list.index(min_odd_num)
                print(f"{min_odd_index}")
    elif current_command[0] == 'first':
        border = int(current_command[1])
        if current_command[2] == 'even':
            if border > len(initial_list):
                print("Invalid count")
            else:
                even_list = [num for num in initial_list if num % 2 == 0]
                if len(even_list) == 0:
                    print("[]")
                else:
                    print(even_list[:border])
        elif current_command[2] == 'odd':
            if border > len(initial_list):
                print("Invalid count")
            else:
                odd_list = [num for num in initial_list if num % 2 != 0]
                if len(odd_list) == 0:
                    print("[]")
                else:
                    print(odd_list[:border])
    elif current_command[0] == 'last':
        border = int(current_command[1])
        if current_command[2] == 'even':
            if border > len(initial_list):
                print("Invalid count")
            else:
                even_list = [num for num in initial_list if num % 2 == 0]
                if len(even_list) == 0:
                    print("[]")
                else:
                    if len(even_list) <= border:
                        print(even_list)
                    else:
                        print(even_list[-border:])
        elif current_command[2] == 'odd':
            if border > len(initial_list):
                print("Invalid count")
            else:
                odd_list = [num for num in initial_list if num % 2 != 0]
                if len(odd_list) == 0:
                    print("[]")
                else:
                    if len(odd_list) <= border:
                        print(odd_list)
                    else:
                        print(odd_list[-border:])

    command = input()

print(initial_list)
