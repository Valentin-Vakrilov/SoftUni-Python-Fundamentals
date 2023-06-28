command = input()

total_coffees = 0

while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        total_coffees += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        total_coffees += 2

    command = input()

if total_coffees <= 5:
    print(total_coffees)
else:
    print("You need extra sleep")
