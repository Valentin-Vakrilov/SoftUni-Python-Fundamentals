def pieces_func(pieces_dict, number):
    for current_piece in range(number):
        command = input().split("|")
        piece = command[0]
        composer = command[1]
        key = command[2]

        pieces_dict[piece] = {"composer": composer, "key": key}

    return pieces_dict


def pieces_command(pieces_dict):

    while True:
        command = input()

        if command == "Stop":
            break

        current_command = command.split("|")
        current_action = current_command[0]
        piece = current_command[1]

        if current_action == "Add":
            if piece in pieces_dict:
                print(f"{piece} is already in the collection!")
            else:
                composer = current_command[2]
                key = current_command[3]
                pieces_dict[piece] = {"composer": composer, "key": key}
                print(f"{piece} by {composer} in {key} added to the collection!")

        elif current_action == "Remove":
            if piece in pieces_dict:
                print(f"Successfully removed {piece}!")
                del pieces_dict[piece]
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")

        elif current_action == "ChangeKey":
            new_key = current_command[2]
            if piece in pieces_dict:
                pieces_dict[piece]["key"] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")


def print_func(pieces_dict):
    for piece in pieces_dict:
        composer = pieces_dict[piece]["composer"]
        key = pieces_dict[piece]["key"]
        print(f"{piece} -> Composer: {composer}, Key: {key}")


def the_pianist(number):
    pieces_dict = {}

    pieces_func(pieces_dict, number)
    pieces_command(pieces_dict)
    print_func(pieces_dict)


number_of_pieces = int(input())
the_pianist(number_of_pieces)
