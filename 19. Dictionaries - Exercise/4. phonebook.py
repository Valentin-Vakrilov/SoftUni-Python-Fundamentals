phonebook_dict = {}

command = input()

while "-" in command:
    current_command = command.split("-")
    name = current_command[0]
    phone_number = current_command[1]
    phonebook_dict[name] = phone_number
    command = input()

number_of_searches = int(command)

for current_search in range(number_of_searches):
    current_name = input()
    if current_name in phonebook_dict.keys():
        print(f"{current_name} -> {phonebook_dict[current_name]}")
    else:
        print(f"Contact {current_name} does not exist.")
