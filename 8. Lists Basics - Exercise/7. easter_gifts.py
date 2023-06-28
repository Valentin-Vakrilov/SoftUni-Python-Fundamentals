gifts_list = input().split()
command = input().split()

final_list = ""

while command[0] != "No" and command[1] != "Money":
    if command[0] == "OutOfStock":
        for gift, value in enumerate(gifts_list):
            if value == command[1]:
                gifts_list[gift] = "None"
    elif command[0] == "Required":
        replace_gift = command[1]
        replace_index = int(command[2])
        if 0 <= replace_index < len(gifts_list):
            gifts_list[replace_index] = replace_gift
    elif command[0] == "JustInCase":
        replacing_gift = command[1]
        gifts_list[-1] = replacing_gift
    command = input().split()

while "None" in gifts_list:
    gifts_list.remove("None")

for gift in gifts_list:
    final_list += str(gift) + " "

print(final_list)
