students_dict = {}

command = input()

while ":" in command:
    current_command = command.split(":")
    name = current_command[0]
    id = current_command[1]
    course = current_command[2]
    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][id] = name
    command = input()

course = " ".join(command.split("_"))

for key, value in students_dict.items():
    if key == course:
        for id, name in value.items():
            print(f"{name} - {id}")
