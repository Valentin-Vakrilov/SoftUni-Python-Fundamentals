student_dict = {}
over_average_dict = {}

number_of_pairs = int(input())

for current_pair in range(number_of_pairs):
    student = input()
    grade = float(input())
    if student not in student_dict:
        student_dict[student] = []
    student_dict[student].append(grade)

for student, grade in student_dict.items():
    for current_grade in grade:
        average_score = sum(student_dict[student]) / len(student_dict[student])
        if average_score >= 4.50:
            over_average_dict[student] = average_score

for student, grade in over_average_dict.items():
    print(f"{student} -> {over_average_dict[student]:.2f}")
