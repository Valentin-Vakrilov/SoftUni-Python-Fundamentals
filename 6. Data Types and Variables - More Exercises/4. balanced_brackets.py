number_of_lines = int(input())

balanced_brackets = 0

for line in range(number_of_lines):
    current_line = input()
    if current_line == "(":
        balanced_brackets += 1
        if balanced_brackets > 1:
            print('UNBALANCED')
            exit()
    elif current_line == ")":
        balanced_brackets -= 1

if balanced_brackets == 0:
    print('BALANCED')
else:
    print('UNBALANCED')
