courses_dict = {}

command = input()

while command != "end":
    current_command = command.split(" : ")
    course = current_command[0]
    student = current_command[1]
    if course not in courses_dict:
        courses_dict[course] = []
    courses_dict[course].append(student)
    command = input()

for course, student in courses_dict.items():
    print(f"{course}: {len(courses_dict[course])}")
    for current_student in student:
        print(f"-- {current_student}")
