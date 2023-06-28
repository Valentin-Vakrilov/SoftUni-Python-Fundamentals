people_waiting = int(input())
state_of_lift = list(map(int, input().split()))

lift_list = []
boarded_people = 0

for lift in range(len(state_of_lift)):
    if people_waiting > 3:
        boarded_people = 4 - state_of_lift[lift]
        people_waiting -= boarded_people
        state_of_lift[lift] += boarded_people
    else:
        state_of_lift[lift] += people_waiting
        people_waiting = 0
    lift_list.append(state_of_lift[lift])

if sum(lift_list) < len(lift_list) * 4:
    print(f"The lift has empty spots!")
elif people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")

print(' '.join(str(number) for number in lift_list))
