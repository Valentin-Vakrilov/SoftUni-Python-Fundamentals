number_of_electrons = int(input())

filled_shells = []

shell_position = 0

while number_of_electrons > 0:
    shell_position += 1
    shell = 2 * (shell_position ** 2)
    if number_of_electrons > shell:
        number_of_electrons -= shell
        filled_shells.append(shell)
    else:
        filled_shells.append(number_of_electrons)
        number_of_electrons = 0

print(filled_shells)
