number_of_rooms = int(input())

total_free_chairs = 0
free_chairs = True

for room in range(1, number_of_rooms+1):
    current_room = input().split()
    number_of_chairs = len(current_room[0])
    number_of_visitors = int(current_room[1])
    if number_of_chairs >= number_of_visitors:
        total_free_chairs += number_of_chairs - number_of_visitors
    else:
        needed_chairs = number_of_visitors - number_of_chairs
        free_chairs = False
        print(f"{needed_chairs} more chairs needed in room {room}")

if free_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
