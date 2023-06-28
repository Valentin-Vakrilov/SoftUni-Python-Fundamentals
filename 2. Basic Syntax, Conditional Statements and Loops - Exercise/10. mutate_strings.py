first_string = input()
second_string = input()

last_string = first_string

for index in range(len(first_string)):
    left_string = second_string[:index+1]
    right_string = first_string[index+1:]
    current_string = left_string + right_string
    if current_string == last_string:
        continue
    last_string = current_string
    print(current_string)
