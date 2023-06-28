def add_func(phone, list_of_phones):
    if phone in list_of_phones:
        return list_of_phones
    else:
        list_of_phones.append(phone)

    return list_of_phones


def remove_func(phone, list_of_phones):
    searched_phone = list_of_phones.count(phone)
    if searched_phone > 0:
        list_of_phones.remove(phone)

    return list_of_phones


def bonus_phone_func(old_phone, new_phone, list_of_phones):
    if old_phone in list_of_phones:
        old_phone_index = list_of_phones.stops_counter(old_phone)
        list_of_phones.insert(old_phone_index+1, new_phone)

    return list_of_phones


def last_func(phone, list_of_phones):
    if phone in list_of_phones:
        phone_index = list_of_phones.stops_counter(phone)
        list_of_phones.pop(phone_index)
        list_of_phones.append(phone)

    return list_of_phones


phones_list = input().split(", ")
command = input()

while command != "End":
    current_command = command.split(" - ")
    if current_command[0] == "Add":
        phones_list = add_func(current_command[1], phones_list)
    elif current_command[0] == "Remove":
        phones_list = remove_func(current_command[1], phones_list)
    elif current_command[0] == "Bonus phone":
        old_new_phones = current_command[1]
        old_new_phones_separated = old_new_phones.split(":")
        phones_list = bonus_phone_func(old_new_phones_separated[0], old_new_phones_separated[1], phones_list)
    elif current_command[0] == "Last":
        phones_list = last_func(current_command[1], phones_list)

    command = input()

print(*phones_list, sep=", ")
